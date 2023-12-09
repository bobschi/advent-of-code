import pytest

from aoc.day09 import (
    get_differences,
    parse_history,
    predict,
    setup_prediction,
    solve_part_a,
    solve_part_b,
)


@pytest.fixture
def histories() -> list[str]:
    return ["0 3 6 9 12 15", "1 3 6 10 15 21", "10 13 16 21 30 45"]


@pytest.fixture
def parsed_histories() -> list[list[int]]:
    return [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]


def test_parse_history(histories: list[str]) -> None:
    assert parse_history(histories[0]) == [0, 3, 6, 9, 12, 15]
    assert parse_history(histories[1]) == [1, 3, 6, 10, 15, 21]
    assert parse_history(histories[2]) == [10, 13, 16, 21, 30, 45]


def test_differences(parsed_histories: list[list[int]]) -> None:
    assert get_differences(parsed_histories[0]) == [3, 3, 3, 3, 3]
    assert get_differences(parsed_histories[1]) == [2, 3, 4, 5, 6]
    assert get_differences(parsed_histories[2]) == [3, 3, 5, 9, 15]


def test_setup_prediction(parsed_histories: list[list[int]]) -> None:
    assert setup_prediction(parsed_histories[0]) == [15, 3, 0]
    assert setup_prediction(parsed_histories[1]) == [21, 6, 1, 0]
    assert setup_prediction(parsed_histories[2]) == [45, 15, 6, 2, 0]


def test_predict(parsed_histories: list[list[int]]) -> None:
    assert predict(parsed_histories[0]) == 18
    assert predict(parsed_histories[1]) == 28
    assert predict(parsed_histories[2]) == 68


def test_solve_part_a(histories: list[str]) -> None:
    assert solve_part_a(histories) == 114


def test_solve_part_b(histories: list[str]) -> None:
    assert solve_part_b(histories) == 2
