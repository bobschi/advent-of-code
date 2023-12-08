import functools
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
    end: Point
    value: str


def parse_numbers(inputs: list[str]) -> list[Number]:
    positions: list[Number] = list()
    for y, line in enumerate(inputs):
        for number in re.finditer(r"\d+", line):
            start = Point(number.start(), y)
            value = number.group()
            end = Point(start.x + len(value) - 1, y)

            if symbol_adjacent(inputs, start, end):
                positions.append(Number(start, end, value))

    return positions


def symbol_adjacent(inputs: list[str], start: Point, end: Point) -> bool:
    line_len = len(inputs[0])
    for y in range(max(start.y - 1, 0), min(line_len, end.y + 2)):
        window = inputs[y][max(start.x - 1, 0) : min(end.x + 2, line_len)]
        if re.findall(r"[^.\d]", window):
            return True

    return False


def solve_part_a(inputs: list[str]) -> int:
    return sum(map(lambda x: int(x.value), parse_numbers(inputs)))


def in_eight_neighborhood(point: Point, number: Number) -> bool:
    for x in range(number.start.x - 1, number.end.x + 2):
        if point.x == x and point.y in range(number.start.y - 1, number.start.y + 2):
            return True

    return False


def find_gear_ratios(inputs: list[str]) -> list[int]:
    numbers = parse_numbers(inputs)
    gear_ratios = list()
    for y, line in enumerate(inputs):
        for potential_gear in re.finditer(r"\*{1}", line):
            gear_pos = Point(potential_gear.start(), y)
            pot_nums = list(filter(lambda n: n.start.y in range(y - 1, y + 2), numbers))
            is_neighbor = functools.partial(in_eight_neighborhood, gear_pos)
            pot_nums = list(filter(is_neighbor, pot_nums))

            if len(pot_nums) == 2:
                gear_ratios.append(int(pot_nums[0].value) * int(pot_nums[1].value))

    return gear_ratios


def solve_part_b(inputs: list[str]) -> int:
    return sum(find_gear_ratios(inputs))


if __name__ == "__main__":
    typer.run(aoc.get_cli(solve_part_a, solve_part_b, 3))
