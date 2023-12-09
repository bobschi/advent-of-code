import pytest

from aoc.day08 import Node, build_graph, get_route, solve_part_a, solve_part_b


@pytest.fixture
def network_map_1() -> list[str]:
    return [
        "RL",
        "",
        "AAA = (BBB, CCC)",
        "BBB = (DDD, EEE)",
        "CCC = (ZZZ, GGG)",
        "DDD = (DDD, DDD)",
        "EEE = (EEE, EEE)",
        "GGG = (GGG, GGG)",
        "ZZZ = (ZZZ, ZZZ)",
    ]


@pytest.fixture
def graph_1() -> dict[str, Node]:
    return dict(
        AAA=Node("BBB", "CCC"),
        BBB=Node("DDD", "EEE"),
        CCC=Node("ZZZ", "GGG"),
        DDD=Node("DDD", "DDD"),
        EEE=Node("EEE", "EEE"),
        GGG=Node("GGG", "GGG"),
        ZZZ=Node("ZZZ", "ZZZ"),
    )


@pytest.fixture
def network_map_3() -> list[str]:
    return [
        "LR",
        ",",
        "11A = (11B, XXX)",
        "11B = (XXX, 11Z)",
        "11Z = (11B, XXX)",
        "22A = (22B, XXX)",
        "22B = (22C, 22C)",
        "22C = (22Z, 22Z)",
        "22Z = (22B, 22B)",
        "XXX = (XXX, XXX)",
    ]


@pytest.fixture
def network_map_2() -> list[str]:
    return ["LLR", "", "AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"]


@pytest.fixture
def graph_2() -> dict[str, Node]:
    return dict(AAA=Node("BBB", "BBB"), BBB=Node("AAA", "ZZZ"), ZZZ=Node("ZZZ", "ZZZ"))


def test_build_graph_1(network_map_1: list[str], graph_1: dict[str, Node]) -> None:
    graph = build_graph(network_map_1[2:])
    assert graph.keys() == graph_1.keys()
    assert all(g == e for g, e in zip(graph.values(), graph_1.values()))


def test_build_graph_2(network_map_2: list[str], graph_2: dict[str, Node]) -> None:
    graph = build_graph(network_map_2[2:])
    assert graph.keys() == graph_2.keys()
    assert all(g == e for g, e in zip(graph.values(), graph_2.values()))


def test_get_route_1(network_map_1: list[str]) -> None:
    directions = network_map_1[0]
    graph = build_graph(network_map_1[2:])

    assert get_route(graph, directions) == ["AAA", "CCC", "ZZZ"]


def test_get_route_2(network_map_2: list[str]) -> None:
    directions = network_map_2[0]
    graph = build_graph(network_map_2[2:])

    expected = ["AAA", "BBB", "AAA", "BBB", "AAA", "BBB", "ZZZ"]
    assert get_route(graph, directions) == expected


def test_solve_part_a(network_map_1: list[str], network_map_2: list[str]) -> None:
    assert solve_part_a(network_map_1) == 2
    assert solve_part_a(network_map_2) == 6


def test_solve_part_b(network_map_3: list[str]) -> None:
    assert solve_part_b(network_map_3) == 6
