import aoc
import day01
import pytest


@pytest.fixture
def part_a_examples() -> list[str]:
    return ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]


def test_first_digit_part_a(part_a_examples: list[str]) -> None:
    expected_first_digits = ["1", "3", "1", "7"]

    for input, expected in zip(part_a_examples, expected_first_digits):
        assert day01.digit(input, day01.Position.FIRST, aoc.Part.A) == expected


def test_last_digit_part_a(part_a_examples: list[str]) -> None:
    expected_last_digits = ["2", "8", "5", "7"]

    for input, expected in zip(part_a_examples, expected_last_digits):
        assert day01.digit(input, day01.Position.LAST, aoc.Part.A) == expected


def test_calibration_value_part_a(part_a_examples: list[str]) -> None:
    expected_calibration_values = [12, 38, 15, 77]

    for input, expected in zip(part_a_examples, expected_calibration_values):
        assert day01.calibration_value(input, aoc.Part.A) == expected


def test_solve_part_a(part_a_examples: list[str]) -> None:
    assert day01.solve(part_a_examples, aoc.Part.A) == 142
