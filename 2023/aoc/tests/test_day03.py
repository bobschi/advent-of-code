import pytest

from aoc.day03 import Number, Point, parse_numbers, solve


@pytest.fixture
def example_schematic() -> list[str]:
    return [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]


def test_parse_numbers(example_schematic) -> None:
    example_positions = [
        Number(Point(0, 0), "467"),
        Number(Point(2, 2), "35"),
        Number(Point(6, 2), "633"),
        Number(Point(0, 4), "617"),
        Number(Point(2, 6), "592"),
        Number(Point(6, 7), "755"),
        Number(Point(1, 9), "664"),
        Number(Point(5, 9), "598"),
    ]

    assert parse_numbers(example_schematic) == example_positions


def test_solve(example_schematic) -> None:
    assert solve(example_schematic) == 4361
