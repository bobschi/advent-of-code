import pytest

from aoc.day04 import Card, parse_card, score, solve_part_a, winning_numbers


@pytest.fixture
def example_scratch_cards() -> list[str]:
    return [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]


@pytest.fixture
def example_expected_cards() -> list[Card]:
    return [
        Card(1, [41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
        Card(2, [13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
        Card(3, [1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]),
        Card(4, [41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),
        Card(5, [87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]),
        Card(6, [31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11]),
    ]


def test_parse_card(example_scratch_cards, example_expected_cards) -> None:
    for i in range(6):
        assert parse_card(example_scratch_cards[i]) == example_expected_cards[i]


def test_winning_numbers(example_expected_cards) -> None:
    assert winning_numbers(example_expected_cards[0]) == [17, 48, 83, 86]
    assert winning_numbers(example_expected_cards[1]) == [32, 61]
    assert winning_numbers(example_expected_cards[2]) == [1, 21]
    assert winning_numbers(example_expected_cards[3]) == [84]
    assert winning_numbers(example_expected_cards[4]) == []
    assert winning_numbers(example_expected_cards[5]) == []


def test_score(example_expected_cards) -> None:
    assert score(example_expected_cards[0]) == 8
    assert score(example_expected_cards[1]) == 2
    assert score(example_expected_cards[2]) == 2
    assert score(example_expected_cards[3]) == 1
    assert score(example_expected_cards[4]) == 0
    assert score(example_expected_cards[5]) == 0


def test_solve_part_a(example_scratch_cards) -> None:
    assert solve_part_a(example_scratch_cards) == 13
