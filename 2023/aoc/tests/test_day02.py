import pytest

from aoc.day02 import (
    Draw,
    Game,
    is_possible_draw,
    is_possible_game,
    parse_draw,
    parse_game,
    possible_game_id,
    solve_part_a,
)


@pytest.fixture
def example_draws_game_1_part_a() -> tuple[list[str], list[Draw]]:
    draws = [Draw(red=4, blue=3), Draw(red=1, green=2, blue=6), Draw(green=2)]
    return ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"], draws


@pytest.fixture
def example_game_1_part_a(example_draws_game_1_part_a) -> tuple[str, Game]:
    expected_game = Game(example_draws_game_1_part_a[1])
    return "; ".join(example_draws_game_1_part_a[0]), expected_game


@pytest.fixture
def example_game_2_part_a() -> tuple[str, Game]:
    draws = [Draw(blue=1, green=2), Draw(green=3, blue=4, red=1), Draw(green=1, blue=1)]
    expected_game = Game(draws)
    return "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", expected_game


@pytest.fixture
def two_example_games(example_game_1_part_a, example_game_2_part_a) -> list[tuple[str, Game]]:
    return [example_game_1_part_a, example_game_2_part_a]


@pytest.fixture
def example_games_part_a(two_example_games) -> list[str]:
    return [
        f"Game 1: {two_example_games[0][0]}",
        f"Game 2: {two_example_games[1][0]}",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]


@pytest.fixture
def bag() -> Draw:
    return Draw(red=4, green=1, blue=7)


@pytest.fixture
def example_bag() -> Draw:
    return Draw(red=12, green=13, blue=14)


def test_parse_draw(example_draws_game_1_part_a) -> None:
    for input, expected in zip(*example_draws_game_1_part_a):
        assert parse_draw(input) == expected


def test_parse_game(two_example_games) -> None:
    for input, expected_game in two_example_games:
        assert parse_game(input) == expected_game


def test_is_possible_draw(bag) -> None:
    draw_plus_expected = [
        (Draw(red=4, blue=3), True),
        (Draw(red=1, green=2, blue=6), False),
        (Draw(green=2), False),
    ]

    for draw, expected in draw_plus_expected:
        assert is_possible_draw(draw, bag) is expected


def test_is_possible_game(bag) -> None:
    game_plus_expected = [
        (Game([Draw(red=4, blue=3), Draw(red=2, green=1)]), True),
        (Game([Draw(red=4, blue=3), Draw(green=2)]), False),
    ]

    for game, expected in game_plus_expected:
        assert is_possible_game(game, bag) is expected


def test_possible_game_id(example_games_part_a, example_bag) -> None:
    expected_ids = [1, 2, 0, 0, 5]

    found_ids = [possible_game_id(game, example_bag) for game in example_games_part_a]

    assert expected_ids == found_ids


def test_solve_part_a(example_games_part_a, example_bag) -> None:
    assert solve_part_a(example_games_part_a, example_bag) == 8
