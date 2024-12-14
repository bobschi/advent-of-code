import pytest

from solutions.day11 import blink, mutate, process_data


@pytest.fixture
def example_input() -> str:
    return "0 1 10 99 999"


@pytest.fixture
def processed_input() -> list[str]:
    return ["0", "1", "10", "99", "999"]


def test_process_data(example_input: str, processed_input: list[str]) -> None:
    assert process_data(example_input) == processed_input


@pytest.mark.parametrize(
    ["stone", "expected"],
    [
        ["0", 1],
        ["1", 1],
        ["2", 1],
        ["10", 2],
        ["99", 2],
        ["999", 1],
        ["1000", 2],
        ["2024",2],
        ["20",2],
        ["24",2],
    ],
)
def test_mutate(stone: int, expected: int | tuple[int, int]) -> None:
    assert mutate(stone) == expected

def test_mutate_multiple_times()->None:
    assert mutate("125",1) == 1
    assert mutate("125",2) == 2
    assert mutate("125",3) == 2
    assert mutate("125",4) == 3
    assert mutate("125",5) == 5
    assert mutate("125",6) == 7

def test_blink() -> None:
    starting = ["125", "17"]
    after_blinks = {1: 3, 2: 4, 3: 5, 4: 9 , 5: 13, 6: 22, 25: 55312}

    for number_of_blinks in range(1, 6):
        assert blink(starting, number_of_blinks) == after_blinks[number_of_blinks]

    assert blink(starting, 25) == after_blinks[25]

