from functools import partial

import pytest

from solutions.day07 import (
    Equation,
    Equations,
    digits,
    ends_with,
    process_data,
    solvable,
)


@pytest.fixture
def example_input() -> str:
    return (
        "190: 10 19\n"
        "3267: 81 40 27\n"
        "83: 17 5\n"
        "156: 15 6\n"
        "7290: 6 8 6 15\n"
        "161011: 16 10 13\n"
        "192: 17 8 14\n"
        "21037: 9 7 18 13\n"
        "292: 11 6 16 20"
    )


@pytest.fixture
def processed_input() -> Equations:
    return [
        Equation([190, 10, 19]),
        Equation([3267, 81, 40, 27]),
        Equation([83, 17, 5]),
        Equation([156, 15, 6]),
        Equation([7290, 6, 8, 6, 15]),
        Equation([161011, 16, 10, 13]),
        Equation([192, 17, 8, 14]),
        Equation([21037, 9, 7, 18, 13]),
        Equation([292, 11, 6, 16, 20]),
    ]


def test_process_data(example_input: str, processed_input: Equations) -> None:
    assert process_data(example_input) == processed_input


def test_has_solution(processed_input: Equations) -> None:
    expected = [True, True, False, False, False, False, False, False, True]

    assert list(map(solvable, processed_input)) == expected


def test_digits() -> None:
    assert digits(1) == 1
    assert digits(21) == 2
    assert digits(321) == 3
    assert digits(4321) == 4
    assert digits(54321) == 5
    assert digits(654321) == 6
    assert digits(7654321) == 7
    assert digits(87654321) == 8
    assert digits(987654321) == 9
    assert digits(1987654321) == 10


def test_ends_with() -> None:
    assert ends_with(1, 1)
    assert not ends_with(2, 1)
    assert ends_with(324, 4)
    assert not ends_with(4327, 6)


def test_has_solution_with_concat(processed_input: Equations) -> None:
    expected = [True, True, False, True, True, False, True, False, True]

    solvable_with_concat = partial(solvable, check_concat=True)

    assert list(map(solvable_with_concat, processed_input)) == expected
