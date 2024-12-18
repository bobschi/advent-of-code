import pytest

from solutions.day04 import (
    Matrix,
    Vector,
    candidates,
    in_bounds,
    number_of_xmas,
    process_data,
    char_coords,
    Dir,
)


@pytest.fixture
def example_input():
    return (
        "MMMSXXMASM\n"
        "MSAMXMSMSA\n"
        "AMXSXMAAMM\n"
        "MSAMASMSMX\n"
        "XMASAMXAMM\n"
        "XXAMMXXAMA\n"
        "SMSMSASXSS\n"
        "SAXAMASAAA\n"
        "MAMMMXMMMM\n"
        "MXMXAXMASX"
    )


@pytest.fixture
def processed_input(example_input: str) -> Matrix:
    return process_data(example_input)


@pytest.fixture
def example_solution():
    return 18


def test_process_data(example_input: str) -> None:
    output = process_data(example_input)

    assert len(output) == 10
    assert all([len(line) == 10 for line in output])
    assert output[0] == ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"]


def test_char_coords(processed_input: Matrix) -> None:
    expected_output = [
        Vector(0, 4),
        Vector(0, 5),
        Vector(1, 4),
        Vector(2, 2),
        Vector(2, 4),
        Vector(3, 9),
        Vector(4, 0),
        Vector(4, 6),
        Vector(5, 0),
        Vector(5, 1),
        Vector(5, 5),
        Vector(5, 6),
        Vector(6, 7),
        Vector(7, 2),
        Vector(8, 5),
        Vector(9, 1),
        Vector(9, 3),
        Vector(9, 5),
        Vector(9, 9),
    ]

    output = char_coords(processed_input)

    assert output == expected_output


def test_in_bounds(processed_input: Matrix) -> None:
    assert not in_bounds(processed_input, Vector(-9999, 0))
    assert not in_bounds(processed_input, Vector(0, -9999))
    assert not in_bounds(processed_input, Vector(9999, 0))
    assert not in_bounds(processed_input, Vector(0, 9999))

    assert in_bounds(processed_input, Vector(0, 0))

    bottom_right = Vector(len(processed_input), len(processed_input[0]))
    assert not in_bounds(processed_input, bottom_right)
    assert in_bounds(processed_input, bottom_right - Vector(1, 1))


def test_candidates(processed_input: Matrix) -> None:
    east = [Vector(0, 0), Vector(0, 1), Vector(0, 2), Vector(0, 3)]
    south_east = [Vector(0, 0), Vector(1, 1), Vector(2, 2), Vector(3, 3)]
    south = [Vector(0, 0), Vector(1, 0), Vector(2, 0), Vector(3, 0)]
    assert candidates(processed_input, Vector(0, 0), Dir.N) == []
    assert candidates(processed_input, Vector(0, 0), Dir.NE) == []
    assert candidates(processed_input, Vector(0, 0), Dir.E) == east
    assert candidates(processed_input, Vector(0, 0), Dir.SE) == south_east
    assert candidates(processed_input, Vector(0, 0), Dir.S) == south
    assert candidates(processed_input, Vector(0, 0), Dir.SW) == []
    assert candidates(processed_input, Vector(0, 0), Dir.W) == []
    assert candidates(processed_input, Vector(0, 0), Dir.NW) == []

    bottom_right = Vector(len(processed_input), len(processed_input[0])) - Vector(1,1)
    assert len(candidates(processed_input, bottom_right, Dir.N)) == 4
    assert candidates(processed_input, bottom_right, Dir.NE) == []
    assert candidates(processed_input, bottom_right, Dir.E) == []
    assert candidates(processed_input, bottom_right, Dir.SE) == []
    assert candidates(processed_input, bottom_right, Dir.S) == []
    assert candidates(processed_input, bottom_right, Dir.SW) == []
    assert len(candidates(processed_input, bottom_right, Dir.W)) == 4
    assert len(candidates(processed_input, bottom_right, Dir.NW)) == 4


def test_number_of_xmas(processed_input: Matrix, example_solution: int) -> None:
    solution = number_of_xmas(processed_input)

    assert solution == example_solution
