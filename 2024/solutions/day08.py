from solutions.shared import Vector
from collections import defaultdict
from itertools import permutations
import aocd
import typer
from copy import deepcopy

app = typer.Typer()


type Positions = list[Vector]
type Frequencies = set[str]


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

    def set_antinode(self, position: Vector) -> None:
        if not is_antenna(self, position):
            self.fields[position.x][position.y] = "#"


def on_map(the_map: Map, position: Vector) -> bool:
    return 0 <= position.x < the_map.len_x() and 0 <= position.y < the_map.len_y()


def is_antenna(the_map: Map, coords: Vector) -> bool:
    return (the_map.get(coords)).isalnum()


def antenna_positions(the_map: Map) -> Positions:
    return [
        vec
        for x in range(the_map.len_x())
        for y in range(the_map.len_y())
        if is_antenna(the_map, vec := Vector(x, y))
    ]


def frequencies(the_map: Map) -> Frequencies:
    return {the_map.get(pos) for pos in antenna_positions(the_map)}


def frequency_groups(the_map: Map) -> dict[str, Positions]:
    groups = defaultdict(list)
    for pos in antenna_positions(the_map):
        groups[the_map.get(pos)].append(pos)
    return groups


def process_data(data: str) -> Map:
    return Map([list(line) for line in data.split("\n")])


def antinodes(the_map: Map) -> Positions:
    possible_positions = []
    for positions in frequency_groups(the_map).values():
        if len(positions) > 1:
            for a, b in permutations(positions, 2):
                possible_positions.append(a - (b - a))

    unique_possible_positions = list(sorted(set(possible_positions)))

    return list({pos for pos in unique_possible_positions if on_map(the_map, pos)})


def visualize(the_map: Map, antinode_positions: Positions | None = None) -> str:
    if antinode_positions is None:
        antinode_positions = []
    visualization = Map(deepcopy(the_map.fields))
    for pos in antinode_positions:
        visualization.set_antinode(pos)
    return "\n".join(["".join(line) for line in visualization.fields])


def harmonic_antinodes(the_map: Map) -> Positions:
    possible_positions = []
    for positions in frequency_groups(the_map).values():
        if len(positions) > 1:
            for a, b in permutations(positions, 2):
                diff = b - a
                scalar = 0
                while on_map(the_map, pos := a - diff.scalar_mult(scalar)):
                    possible_positions.append(pos)
                    scalar = scalar + 1

    unique_possible_positions = list(sorted(set(possible_positions)))

    return list({pos for pos in unique_possible_positions if on_map(the_map, pos)})


@app.command()
def part_1() -> None:
    solution = len(antinodes(process_data(aocd.get_data(day=8, year=2024))))
    aocd.submit(str(solution), part="a", day=8, year=2024)

@app.command()
def part_2() -> None:
    solution = len(harmonic_antinodes(process_data(aocd.get_data(day=8, year=2024))))
    aocd.submit(str(solution), part="b", day=8, year=2024)


if __name__ == "__main__":
    app()
