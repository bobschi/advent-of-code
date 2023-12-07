import re
import enum
import aocd
import argparse


class Position(enum.IntEnum):
    FIRST = 0
    LAST = -1


class Part(enum.StrEnum):
    A = "a"
    B = "b"


def digit(input: str, position: Position, part: Part) -> str:
    return re.findall("\d", input)[position.value]


def calibration_value(input: str, part: Part) -> int:
    return int(digit(input, Position.FIRST, part) + digit(input, Position.LAST, part))


def solve(input: list[str], part: Part) -> int:
    return sum(map(calibration_value, input, part * len(input)))


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument("part", choices=["a", "b"])

    inputs = aocd.get_data(day=1, year=2023).split("\n")
    if (part := Part(parser.parse_args().part)) == Part.A:
        aocd.submit(solve(inputs, part), part.value, day=1, year=2023)


if __name__ == "__main__":
    __main__()
