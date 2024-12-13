from collections import defaultdict, deque
from copy import deepcopy
from enum import StrEnum

import aocd
import typer
from rich.progress import track

from solutions.shared import Dir, Vector


class Marks(StrEnum):
    GUARD = "^"
    OBSTRUCTION = "#"
    VISITED = "X"
    NEW_OBSTRUCTION = "O"


app = typer.Typer()

type Movements = list[Vector]


class Map:
    fields: list[list[str]]

    def __init__(self, fields: list[list[str]]) -> None:
        self.fields = fields

    def __eq__(self, other) -> bool:
        return self.fields == other.fields

    def __repr__(self) -> str:
        return f"Map {len(self.fields)}x{len(self.fields[0])}"

    def get(self, coords: Vector) -> str:
        return self.fields[coords.x][coords.y]

    def len_x(self) -> int:
        return len(self.fields)

    def len_y(self) -> int:
        return len(self.fields[0])

    def set(self, coords: Vector, mark: str) -> None:
        self.fields[coords.x][coords.y] = mark

    def visit(self, coords: Vector) -> None:
        self.set(coords, Marks.VISITED)

    def obstruct(self, coords: Vector) -> None:
        self.set(coords, Marks.NEW_OBSTRUCTION)

    def is_obstructed(self, coords: Vector) -> bool:
        return self.get(coords) in [Marks.OBSTRUCTION, Marks.NEW_OBSTRUCTION]

    def new_obstruction_position(self) -> Vector:
        for x, line in enumerate(self.fields):
            if Marks.NEW_OBSTRUCTION in line:
                return Vector(x, line.index(Marks.NEW_OBSTRUCTION))
        return Vector(-1, -1)


class Route:
    the_map: Map
    movements: Movements
    directions: dict[Vector, list[Dir]]
    is_loop: bool = False

    def __init__(self, the_map: Map) -> None:
        self.the_map = the_map
        self.movements = []
        self.directions = defaultdict(list)

    def add(self, position: Vector, direction: Dir) -> None:
        self.movements.append(position)
        self.directions[position].append(direction)


def is_loop(position: Vector, direction: Dir, route: Route) -> bool:
    return direction in route.directions[position]


def in_bounds(the_map: Map, position: Vector) -> bool:
    return 0 <= position.x < the_map.len_x() and 0 <= position.y < the_map.len_y()


def process_data(data: str) -> Map:
    return Map([list(line) for line in data.split("\n")])


def guard_position(the_map: Map) -> Vector:
    for x, line in enumerate(the_map.fields):
        for y, cell in enumerate(line):
            if cell == Marks.GUARD:
                return Vector(x, y)

    return Vector(-1, -1)


def calculate_guard_route(the_map: Map) -> Route:
    route = Route(the_map)
    possible_directions = deque(Dir.cardinals())
    current_direction = possible_directions.popleft()
    current_position = guard_position(the_map)

    while in_bounds(the_map, current_position):
        if is_loop(current_position, current_direction, route):
            route.is_loop = True
            break
        if the_map.is_obstructed(current_position):
            current_position = current_position - current_direction.value
            possible_directions.append(current_direction)
            current_direction = possible_directions.popleft()
        else:
            route.add(current_position, current_direction)
        current_position = current_position + current_direction.value

    return route


def find_loops(the_map: Map) -> list[Route]:
    initial_route = calculate_guard_route(the_map)
    loops = []

    for position in track(initial_route.movements):
        if the_map.get(position) in [Marks.GUARD, Marks.OBSTRUCTION]:
            continue
        new_map = Map(deepcopy(the_map.fields))
        new_map.obstruct(position)
        potential_route = calculate_guard_route(new_map)
        if potential_route.is_loop:
            loops.append(potential_route)

    return loops


def visualize_route(the_map: Map, route: Route | None = None) -> None:
    visualize_this = Map(deepcopy(the_map.fields))
    if route:
        if route.is_loop:
            print("Is loop.")
        else:
            print("No loop.")
        for position in route.movements:
            visualize_this.visit(position)
    for line in visualize_this.fields:
        print("".join(line))


def possible_new_obstructions(loops: list[Route]) -> set[Vector]:
    return {loop.the_map.new_obstruction_position() for loop in loops}


@app.command()
def part1() -> None:
    data = aocd.get_data(day=6, year=2024)
    the_map = process_data(data)
    route = calculate_guard_route(the_map)
    aocd.submit(answer=str(len(set(route.movements))), part="a", day=6, year=2024)


@app.command()
def part2() -> None:
    data = aocd.get_data(day=6, year=2024)
    the_map = process_data(data)
    new_obstructions = possible_new_obstructions(find_loops(the_map))
    aocd.submit(answer=str(len(new_obstructions)), part="b", day=6, year=2024)


if __name__ == "__main__":
    app()
