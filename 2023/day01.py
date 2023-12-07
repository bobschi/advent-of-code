import re
import enum
import aocd
import aoc
import typer


class Position(enum.IntEnum):
    FIRST = 0
    LAST = -1


def digit(input: str, position: Position, part: aoc.Part) -> str:
    return re.findall("\d", input)[position.value]


def calibration_value(input: str, part: aoc.Part) -> int:
    return int(digit(input, Position.FIRST, part) + digit(input, Position.LAST, part))


def solve(input: list[str], part: aoc.Part) -> int:
    return sum(map(calibration_value, input, part * len(input)))


def main(part: str) -> None:
    part = aoc.Part(part)
    inputs = aocd.get_data(day=1, year=2023).split("\n")
    aocd.submit(solve(inputs, part), part.value, day=1, year=2023)


if __name__ == "__main__":
    typer.run(main)
