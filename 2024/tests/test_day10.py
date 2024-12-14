from functools import partial

import pytest

from solutions.day10 import (
    Dir,
    Map,
    Trails,
    Vector,
    find_number_coords,
    find_trails,
    four_neighborhood,
    in_bounds,
    score,
    process_map,
    rate_trails,
)


@pytest.fixture
def example_1() -> str:
    # 1 trailhead, score 1
    return "0123\n" "1234\n" "8765\n" "9876"


@pytest.fixture
def example_1_map() -> Map:
    return Map([[0, 1, 2, 3], [1, 2, 3, 4], [8, 7, 6, 5], [9, 8, 7, 6]])


@pytest.fixture
def example_2() -> str:
    # 1 trailhead, score 2
    return (
        "1120211\n"
        "1111111\n"
        "2222222\n"
        "6543456\n"
        "7111117\n"
        "8111118\n"
        "9111119"
    )


@pytest.fixture
def example_3() -> str:
    # score 4
    return (
        "1190229\n"
        "1111198\n"
        "2222227\n"
        "6543456\n"
        "7652987\n"
        "8762222\n"
        "9872222"
    )


@pytest.fixture
def example_4() -> str:
    # 2 trailheads, score 1 and score 2
    return (
        "1022922\n"
        "2222822\n"
        "3222722\n"
        "4567654\n"
        "2228223\n"
        "2229222\n"
        "2222201"
    )


@pytest.fixture
def example_5() -> str:
    # 9 trailheads, scores 5, 6, 5, 3, 1, 3, 5, 3, and 5
    return (
        "89010123\n"
        "78121874\n"
        "87430965\n"
        "96549874\n"
        "45678903\n"
        "32019012\n"
        "01329801\n"
        "10456732"
    )


@pytest.fixture
def example_6() -> str:
    return "012345\n" "123456\n" "234567\n" "345678\n" "496789\n" "567891"


def test_process_map(example_1: str, example_1_map: Map) -> None:
    assert process_map(example_1) == example_1_map


def test_in_bounds(example_1_map: Map) -> None:
    assert not in_bounds(example_1_map, Vector(-1, -1))
    assert not in_bounds(example_1_map, Vector(0, -1))
    assert not in_bounds(example_1_map, Vector(-1, 0))

    len_x = example_1_map.len_x()
    len_y = example_1_map.len_y()
    assert in_bounds(example_1_map, Vector(0, 0))
    assert in_bounds(example_1_map, Vector(0, len_y - 1))
    assert in_bounds(example_1_map, Vector(len_x - 1, 0))
    assert in_bounds(example_1_map, Vector(len_x - 1, len_y - 1))

    assert not in_bounds(example_1_map, Vector(0, len_y))
    assert not in_bounds(example_1_map, Vector(len_x, 0))
    assert not in_bounds(example_1_map, Vector(len_x, len_y))


@pytest.mark.parametrize(
    ["coords", "expected"],
    [
        [Vector(0, 0), {Dir.E: 1, Dir.S: 1}],
        [Vector(1, 0), {Dir.N: 0, Dir.E: 2, Dir.S: 8}],
        [Vector(0, 1), {Dir.E: 2, Dir.S: 2, Dir.W: 0}],
        [Vector(1, 1), {Dir.N: 1, Dir.E: 3, Dir.S: 7, Dir.W: 1}],
    ],
)
def test_four_neighborhood(
    coords: Vector, expected: dict[Dir, int], example_1_map: Map
) -> None:
    _four_neighborhood = partial(four_neighborhood, example_1_map)
    assert _four_neighborhood(coords) == expected


def test_find_number_coords(example_1_map: Map) -> None:
    assert list(find_number_coords(example_1_map, 9)) == [Vector(3, 0)]
    assert list(find_number_coords(example_1_map, 0)) == [Vector(0, 0)]


@pytest.mark.parametrize(
    ["input_fixture", "expected"],
    [
        ["example_1", {Vector(0, 0): {Vector(3, 0)}}],
        ["example_2", {Vector(0, 3): {Vector(6, 0), Vector(6, 6)}}],
        [
            "example_3",
            {Vector(0, 3): {Vector(0, 6), Vector(1, 5), Vector(4, 4), Vector(6, 0)}},
        ],
        [
            "example_4",
            {
                Vector(0, 1): {Vector(5, 3)},
                Vector(6, 5): {Vector(0, 4), Vector(5, 3)},
            },
        ],
    ],
)
def test_find_trails(input_fixture: str, expected: Trails, request) -> None:
    the_map = process_map(request.getfixturevalue(input_fixture))
    assert find_trails(the_map) == expected


@pytest.mark.parametrize(
    ["input_fixture", "expected"],
    [
        ["example_1", 1],
        ["example_2", 2],
        ["example_3", 4],
        ["example_4", 3],
        ["example_5", 36],
    ],
)
def test_score(input_fixture: str, expected: int, request) -> None:
    the_map = process_map(request.getfixturevalue(input_fixture))
    assert score(find_trails(the_map)) == expected


def test_rate_trails(example_6: str) -> None:
    assert rate_trails(process_map(example_6)) == 227
