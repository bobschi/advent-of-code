import aocd
import typer
from functools import lru_cache

app = typer.Typer()


def process_data(data: str) -> list[str]:
    return list(data.split(" "))


@lru_cache(maxsize=None)
def mutate(stone: str, blinks_to_go: int = 1) -> int:
    if blinks_to_go == 0:
        return 1
    
    elif stone == "0":
        return mutate("1", blinks_to_go - 1)
    
    elif len(stone) % 2 == 0:
        middle = len(stone) // 2
        left = str(int(stone[:middle]))
        right = str(int(stone[middle:]))
        return mutate(left, blinks_to_go - 1) + mutate(right, blinks_to_go - 1)
    return mutate(str(int(stone) * 2024), blinks_to_go - 1)


def blink(stones: list[str], times: int) -> int:
    return sum([mutate(stone,times) for stone in stones])


@app.command()
def part_1() -> None:
    answer = blink(process_data(aocd.get_data(day=11, year=2024)), 25)
    aocd.submit(str(answer), part="a", day=11, year=2024)


@app.command()
def part_2() -> None:
    answer = blink(process_data(aocd.get_data(day=11, year=2024)), 75)
    aocd.submit(str(answer), part="b", day=11, year=2024)


if __name__ == "__main__":
    app()
