import math
import re
from dataclasses import dataclass
from itertools import cycle

import typer

from aoc.infra import get_cli


@dataclass
class Node:
    left: str
    right: str


def build_graph(inputs: list[str]):
    graph: dict[str, Node] = {}

    for line in inputs:
        name, left, right = re.findall(r"\w{3}", line)
        graph[name] = Node(left, right)

    return graph


def get_next_node_name(node: Node, direction: str) -> str:
    if direction == "L":
        return node.left
    return node.right


def get_route(
    graph: dict[str, Node],
    directions: str,
    start_node: str = "AAA",
    end_nodes: list[str] = ["ZZZ"],
) -> list[str]:
    direction = cycle(list(directions))
    visited = [start_node]

    while visited[-1] not in end_nodes:
        current_node = graph[visited[-1]]
        visited.append(get_next_node_name(current_node, next(direction)))

    return visited


def solve_part_a(inputs: list[str]) -> int:
    directions = inputs[0]

    graph = build_graph(inputs[2:])
    route = get_route(graph, directions)

    return len(route) - 1


def solve_part_b(inputs: list[str]) -> int:
    directions = inputs[0]
    graph = build_graph(inputs[2:])

    start_nodes = [node for node in graph.keys() if node.endswith("A")]
    end_nodes = [node for node in graph.keys() if node.endswith("Z")]
    routes = [get_route(graph, directions, node, end_nodes) for node in start_nodes]
    route_lengths = [length - 1 for length in map(len, routes)]

    return math.lcm(*route_lengths)


if __name__ == "__main__":
    typer.run(get_cli(solve_part_a, solve_part_b, 8))
