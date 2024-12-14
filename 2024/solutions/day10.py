from collections import defaultdict
from typing import Generator

import aocd
import typer

from solutions.shared import Dir, Vector

app = typer.Typer()


type Trails = dict[Vector, set[Vector]]


class Map:
    fields: list[list[int]]

    def __init__(self, fields: list[list[int]]) -> None:
        self.fields = fields

    def __eq__(self, other) -> bool:
        return self.fields == other.fields

    def __repr__(self) -> str:
        return f"Map {len(self.fields)}x{len(self.fields[0])}"

    def get(self, coords: Vector) -> int:
        return self.fields[coords.x][coords.y]

    def len_x(self) -> int:
        return len(self.fields)

    def len_y(self) -> int:
        return len(self.fields[0])


def process_map(data: str) -> Map:
    return Map([list(map(int, line)) for line in data.split("\n")])


def in_bounds(the_map: Map, coords: Vector) -> bool:
    return 0 <= coords.x < the_map.len_x() and 0 <= coords.y < the_map.len_y()


def four_neighborhood(the_map: Map, coords: Vector) -> dict[Dir, int]:
    return {
        direction: the_map.get(neighbor)
        for direction in Dir.cardinals()
        if in_bounds(the_map, neighbor := coords + direction.value)
    }


def find_number_coords(the_map: Map, number: int) -> Generator[Vector, None, None]:
    return (
        Vector(x, y)
        for x, line in enumerate(the_map.fields)
        for y, height in enumerate(line)
        if height == number
    )


def find_trails(the_map: Map) -> Trails:
    trails = defaultdict(set)

    for trailhead in set(find_number_coords(the_map, 0)):
        trails[trailhead] = search_reachable_nines(the_map, trailhead)

    return trails


def search_reachable_nines(the_map: Map, coords: Vector) -> set[Vector]:
    next_height = the_map.get(coords) + 1
    if next_height == 10:
        return {coords}

    solution = set()
    for direction, height in four_neighborhood(the_map, coords).items():
        if height == next_height:
            solution |= search_reachable_nines(the_map, coords + direction.value)

    return solution


def score(trails: Trails) -> int:
    return sum(len(nines) for nines in trails.values())


def rate_trails(the_map: Map) -> int:
    trails = defaultdict(list)

    def search_reachable_nines(coords: Vector) -> list[Vector]:
        next_height = the_map.get(coords) + 1
        if next_height == 10:
            return [coords]

        solution = list()
        for direction, height in four_neighborhood(the_map, coords).items():
            if height == next_height:
                solution += search_reachable_nines(coords + direction.value)

        return solution

    for trailhead in set(find_number_coords(the_map, 0)):
        trails[trailhead] = search_reachable_nines(trailhead)

    return sum(len(nines) for nines in trails.values())


@app.command()
def part_1() -> None:
    answer = score(find_trails(process_map(aocd.get_data(day=10, year=2024))))
    aocd.submit(answer=str(answer), part="a", day=10, year=2024)


@app.command()
def part_2() -> None:
    answer = rate_trails(process_map(aocd.get_data(day=10, year=2024)))
    aocd.submit(answer=str(answer), part="b", day=10, year=2024)


if __name__ == "__main__":
    app()
