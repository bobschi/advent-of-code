import re
from dataclasses import dataclass

import typer

import aoc.infra as aoc


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Number:
    start: Point
    value: str


def parse_numbers(inputs: list[str]) -> list[Number]:
    positions: list[Number] = list()
    for y, line in enumerate(inputs):
        for number in re.finditer(r"\d+", line):
            start = Point(number.start(), y)
            value = number.group()

            if symbol_adjacent(inputs, start, Point(start.x + len(value) - 1, start.y)):
                positions.append(Number(start, value))

    return positions


def symbol_adjacent(inputs: list[str], start: Point, end: Point) -> bool:
    line_len = len(inputs[0])
    for y in range(max(start.y - 1, 0), min(line_len, end.y + 2)):
        window = inputs[y][max(start.x - 1, 0) : min(end.x + 2, line_len)]
        if re.findall(r"[^.\d]", window):
            return True

    return False


def solve(inputs: list[str]) -> int:
    return sum(map(lambda x: int(x.value), parse_numbers(inputs)))


if __name__ == "__main__":
    typer.run(aoc.get_cli(solve, None, 3))
