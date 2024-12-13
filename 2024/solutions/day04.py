from __future__ import annotations

import aocd
import typer

from solutions.shared import Vector, Dir

app = typer.Typer()


Matrix = list[list[str]]




def get_char(input: Matrix, coord: Vector) -> str:
    return input[coord.x][coord.y]


def process_data(input: str) -> Matrix:
    return list(map(list, input.split("\n")))


def char_coords(input: Matrix, char: str = "X") -> list[Vector]:
    return [
        Vector(x, y)
        for x, line in enumerate(input)
        for y, character in enumerate(line)
        if character == char
    ]


def in_bounds(input: Matrix, coord: Vector) -> bool:
    return 0 <= coord.x < len(input) and 0 <= coord.y < len(input[0])


def candidates(input: Matrix, coord: Vector, direction: Dir) -> list[Vector]:
    coords = [coord + direction.value.scalar_mult(factor) for factor in range(0, 4)]

    if not all([in_bounds(input, coord) for coord in coords]):
        return []

    return coords


def number_of_xmas(input: Matrix) -> int:
    hits = 0
    for x_coord in char_coords(input):
        for direction in Dir.all():
            coords = candidates(input, x_coord, direction)
            if coords:
                word = "".join([get_char(input, coord) for coord in coords])
                if word == "XMAS":
                    hits = hits + 1
    return hits


def is_mas(word: str) -> bool:
    return word == "MAS" or word == "SAM"


def number_of_x_mas(input: Matrix) -> int:
    hits = 0
    for a_coord in char_coords(input, "A"):
        word_1_coords = [a_coord + Dir.NW.value, a_coord, a_coord + Dir.SE.value]
        word_2_coords = [a_coord + Dir.NE.value, a_coord, a_coord + Dir.SW.value]

        if not all([in_bounds(input, c) for c in word_1_coords + word_2_coords]):
            continue

        word_1 = "".join([get_char(input, c) for c in word_1_coords])
        word_2 = "".join([get_char(input, c) for c in word_2_coords])
        if is_mas(word_1) and is_mas(word_2):
            hits = hits + 1

    return hits


@app.command()
def part1() -> None:
    matrix = process_data(aocd.get_data(day=4, year=2024))
    aocd.submit(str(number_of_xmas(matrix)), part="a", day=4, year=2024)


@app.command()
def part2() -> None:
    matrix = process_data(aocd.get_data(day=4, year=2024))
    aocd.submit(str(number_of_x_mas(matrix)), part="b", day=4, year=2024)
