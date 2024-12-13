from enum import IntEnum

import aocd
import pydantic
import typer
from rich.progress import track

app = typer.Typer()


class BlockType(IntEnum):
    FILE = 0
    FREE_SPACE = -1


class File(pydantic.BaseModel):
    id: int
    length: int

    def __repr__(self) -> str:
        return str(self.id) * self.length

    def __str__(self) -> str:
        return self.__repr__()


class FreeSpace(pydantic.BaseModel):
    id: int = BlockType.FREE_SPACE.value
    length: int

    def __repr__(self) -> str:
        return "." * self.length

    def __str__(self) -> str:
        return self.__repr__()


type FileStream = list[File | FreeSpace]
type IdList = list[int]


def process_data(data: str) -> FileStream:
    return [
        File(id=current_id // 2, length=int(space))
        if current_id % 2 == BlockType.FILE
        else FreeSpace(length=int(space))
        for current_id, space in enumerate(data)
    ]


def defrag(file_stream: FileStream) -> IdList:
    id_list = []

    for file in file_stream:
        id_list.extend([file.id for _ in range(file.length)])

    for index, file_id in enumerate(id_list):
        last_defragged_index = len(id_list) - 1
        if file_id == BlockType.FREE_SPACE:
            for defrag_index in range(last_defragged_index, 0, -1):
                if index == defrag_index:
                    return id_list

                if id_list[defrag_index] != BlockType.FREE_SPACE:
                    id_list[index] = id_list[defrag_index]
                    id_list[defrag_index] = BlockType.FREE_SPACE.value
                    last_defragged_index = defrag_index
                    break

    return id_list


def checksum(id_list: IdList) -> int:
    return sum(
        index * file_id
        for index, file_id in enumerate(id_list)
        if file_id != BlockType.FREE_SPACE
    )


def file_defrag(file_stream: FileStream) -> IdList:
    for file in track(reversed(file_stream)):
        if file.id == BlockType.FREE_SPACE:
            continue
        index = file_stream.index(file)
        for candidate_index, candidate in enumerate(file_stream[:index]):
            if candidate.id != BlockType.FREE_SPACE:
                continue
            if candidate.length == file.length:
                file_stream[index] = candidate
                file_stream[candidate_index] = file
                break
            elif candidate.length > file.length:
                rest_length = candidate.length - file.length
                file_stream[index] = FreeSpace(length=file.length)
                file_stream.insert(candidate_index + 1, FreeSpace(length=rest_length))
                file_stream[candidate_index] = file
                break

    return [file.id for file in file_stream for _ in range(file.length)]


def visualize(file_stream: FileStream) -> str:
    return "".join(map(str, file_stream))


@app.command()
def part_1() -> None:
    answer = checksum(defrag(process_data(aocd.get_data(day=9, year=2024))))
    aocd.submit(answer=str(answer), part="a", day=9, year=2024)


@app.command()
def part_2() -> None:
    answer = checksum(file_defrag(process_data(aocd.get_data(day=9, year=2024))))
    aocd.submit(answer=str(answer), part="b", day=9, year=2024)
