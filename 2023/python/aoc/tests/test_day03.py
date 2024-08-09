import pytest

from aoc.day03 import Number, Point, find_gear_ratios, parse_numbers, solve_part_a


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
        Number(Point(0, 0), Point(2, 0), "467"),
        Number(Point(2, 2), Point(3, 2), "35"),
        Number(Point(6, 2), Point(8, 2), "633"),
        Number(Point(0, 4), Point(2, 4), "617"),
        Number(Point(2, 6), Point(4, 6), "592"),
        Number(Point(6, 7), Point(8, 7), "755"),
        Number(Point(1, 9), Point(3, 9), "664"),
        Number(Point(5, 9), Point(7, 9), "598"),
    ]

    assert parse_numbers(example_schematic) == example_positions


def test_solve(example_schematic) -> None:
    assert solve_part_a(example_schematic) == 4361


def test_find_gear_ratios(example_schematic) -> None:
    expected_ratios = [16345, 451490]

    assert find_gear_ratios(example_schematic) == expected_ratios
