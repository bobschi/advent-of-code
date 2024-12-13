import pytest

from solutions.day08 import (
    Map,
    process_data,
    Vector,
    is_antenna,
    antenna_positions,
    Positions,
    frequencies,
    frequency_groups,
    on_map,
    antinodes,
    visualize,
    harmonic_antinodes,
)


@pytest.fixture
def example_input() -> str:
    return (
        "............\n"
        "........0...\n"
        ".....0......\n"
        ".......0....\n"
        "....0.......\n"
        "......A.....\n"
        "............\n"
        "............\n"
        "........A...\n"
        ".........A..\n"
        "............\n"
        "............"
    )


@pytest.fixture
def example_map() -> Map:
    return Map(
        [
            list("............"),
            list("........0..."),
            list(".....0......"),
            list(".......0...."),
            list("....0......."),
            list("......A....."),
            list("............"),
            list("............"),
            list("........A..."),
            list(".........A.."),
            list("............"),
            list("............"),
        ]
    )


@pytest.fixture
def case_2() -> Map:
    return Map(
        [
            list(".........."),
            list("...#......"),
            list(".........."),
            list("....a....."),
            list(".........."),
            list(".....a...."),
            list(".........."),
            list("......#..."),
            list(".........."),
            list(".........."),
        ]
    )


@pytest.fixture
def case_3() -> Map:
    return Map(
        [
            list(".........."),
            list("...#......"),
            list("#........."),
            list("....a....."),
            list("........a."),
            list(".....a...."),
            list("..#......."),
            list("......#..."),
            list(".........."),
            list(".........."),
        ]
    )


@pytest.fixture
def case_4() -> Map:
    return Map(
        [
            list(".........."),
            list("...#......"),
            list("#........."),
            list("....a....."),
            list("........a."),
            list(".....a...."),
            list("..#......."),
            list("......A..."),
            list(".........."),
            list(".........."),
        ]
    )


@pytest.fixture
def case_5() -> Map:
    return Map(
        [
            list("......#....#"),
            list("...#....0..."),
            list("....#0....#."),
            list("..#....0...."),
            list("....0....#.."),
            list(".#....A....."),
            list("...#........"),
            list("#......#...."),
            list("........A..."),
            list(".........A.."),
            list("..........#."),
            list("..........#."),
        ]
    )


@pytest.fixture
def antenna_coords() -> Positions:
    return [
        Vector(1, 8),
        Vector(2, 5),
        Vector(3, 7),
        Vector(4, 4),
        Vector(5, 6),
        Vector(8, 8),
        Vector(9, 9),
    ]


@pytest.fixture
def part_2_case_1() -> Map:
    return Map(
        [
            list("T....#...."),
            list("...T......"),
            list(".T....#..."),
            list(".........#"),
            list("..#......."),
            list(".........."),
            list("...#......"),
            list(".........."),
            list("....#....."),
            list(".........."),
        ]
    )


@pytest.fixture
def part_2_case_2() -> Map:
    return Map(
        [
            list("##....#....#"),
            list(".#.#....0..."),
            list("..#.#0....#."),
            list("..##...0...."),
            list("....0....#.."),
            list(".#...#A....#"),
            list("...#..#....."),
            list("#....#.#...."),
            list("..#.....A..."),
            list("....#....A.."),
            list(".#........#."),
            list("...#......##"),
        ]
    )


def test_process_data(example_input: str, example_map: Map) -> None:
    assert process_data(example_input) == example_map


def test_is_antenna(example_map: Map, antenna_coords: Positions) -> None:
    not_antenna_coords = [Vector(0, 0), Vector(1, 2), Vector(8, 9)]

    assert not any([is_antenna(example_map, coords) for coords in not_antenna_coords])
    assert all([is_antenna(example_map, coords) for coords in antenna_coords])


def test_antenna_positions(example_map: Map, antenna_coords: Positions) -> None:
    assert antenna_positions(example_map) == antenna_coords


@pytest.mark.parametrize(
    ["case_name", "expected_frequencies"],
    [
        ["example_map", {"0", "A"}],
        ["case_2", {"a"}],
        ["case_3", {"a"}],
        ["case_4", {"a", "A"}],
        ["case_5", {"0", "A"}],
    ],
)
def test_frequencies(case_name: str, expected_frequencies: set[str], request) -> None:
    map: Map = request.getfixturevalue(case_name)
    assert frequencies(map) == expected_frequencies


def test_frequency_groups(example_map: Map, antenna_coords: Positions) -> None:
    expected_groups = {
        "0": antenna_coords[:4],
        "A": antenna_coords[4:],
    }
    assert frequency_groups(example_map) == expected_groups


@pytest.mark.parametrize(
    ["position", "result"],
    [
        [Vector(-1, -1), False],
        [Vector(0, -1), False],
        [Vector(-1, 0), False],
        [Vector(0, 0), True],
        [Vector(9999, 9999), False],
        [Vector(9999, 10), False],
        [Vector(10, 9999), False],
        [Vector(10, 10), True],
    ],
)
def test_on_map(example_map: Map, position: Vector, result: bool) -> None:
    assert on_map(example_map, position) is result


def test_visualize(example_map: Map, example_input: str) -> None:
    assert visualize(example_map) == example_input


@pytest.mark.parametrize("case_name", ["case_2", "case_3", "case_4", "case_5"])
def test_antinodes(case_name: str, request) -> None:
    the_map = request.getfixturevalue(case_name)

    assert visualize(the_map, antinodes(the_map)) == visualize(the_map)


def test_antinodes_case_3(case_3: Map) -> None:
    expected_antinodes = [Vector(1, 3), Vector(6, 2), Vector(7, 6), Vector(2, 0)]

    assert antinodes(case_3) == expected_antinodes


@pytest.mark.parametrize(
    ["case_name", "num_antinodes"],
    [
        ["case_2", 2],
        ["case_3", 4],
        ["case_4", 4],
        ["case_5", 14],
    ],
)
def test_num_antinodes(case_name: str, num_antinodes: int, request) -> None:
    the_map = request.getfixturevalue(case_name)

    assert len(antinodes(the_map)) == num_antinodes


@pytest.mark.parametrize(
    ["case_name", "num_antinodes"], [["part_2_case_1", 9], ["part_2_case_2", 34]]
)
def test_num_harmonic_antinodes(case_name: str, num_antinodes: int, request) -> None:
    the_map = request.getfixturevalue(case_name)

    assert len(harmonic_antinodes(the_map)) == num_antinodes
