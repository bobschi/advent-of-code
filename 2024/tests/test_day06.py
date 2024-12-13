import pytest

from solutions.day06 import (
    Map,
    find_loops,
    possible_new_obstructions,
    process_data,
    guard_position,
    Vector,
    in_bounds,
    calculate_guard_route,
)


@pytest.fixture
def example_input() -> str:
    return (
        "....#.....\n"
        ".........#\n"
        "..........\n"
        "..#.......\n"
        ".......#..\n"
        "..........\n"
        ".#..^.....\n"
        "........#.\n"
        "#.........\n"
        "......#..."
    )


@pytest.fixture
def processed_map() -> Map:
    return Map(
        [
            [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "#", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "#", ".", ".", "^", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
        ]
    )


def test_import_data(example_input: str, processed_map: Map) -> None:
    assert process_data(example_input) == processed_map


def test_guard_position(processed_map: Map) -> None:
    assert guard_position(processed_map) == Vector(6, 4)


def test_in_bounds(processed_map: Map) -> None:
    bottom_right = Vector(processed_map.len_x(), processed_map.len_y()) - Vector(1, 1)
    assert in_bounds(processed_map, Vector(0, 0))
    assert in_bounds(processed_map, bottom_right)
    assert in_bounds(processed_map, Vector(5, 5))

    assert not in_bounds(processed_map, Vector(-1, -1))
    assert not in_bounds(processed_map, Vector(0, -1))
    assert not in_bounds(processed_map, Vector(-1, 0))
    assert not in_bounds(processed_map, Vector(9999, 9999))
    assert not in_bounds(processed_map, Vector(0, 9999))
    assert not in_bounds(processed_map, Vector(9999, 0))


def test_calculate_guard_route(processed_map: Map) -> None:
    route = calculate_guard_route(processed_map)
    assert len(set(route.movements)) == 41


def test_find_loops(processed_map: Map) -> None:
    expected_positions = {
        Vector(6, 3),
        Vector(7, 6),
        Vector(7, 7),
        Vector(8, 1),
        Vector(8, 3),
        Vector(9, 7),
    }
    loops = find_loops(processed_map)
    positions = {loop.the_map.new_obstruction_position() for loop in loops}

    assert positions == expected_positions


def test_possible_new_obstructions(processed_map: Map) -> None:
    expected_positions = {
        Vector(6, 3),
        Vector(7, 6),
        Vector(7, 7),
        Vector(8, 1),
        Vector(8, 3),
        Vector(9, 7),
    }
    new_obstructions = possible_new_obstructions(find_loops(processed_map))

    assert new_obstructions == expected_positions
