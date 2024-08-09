from dataclasses import dataclass, field

import aocd
import typer

import aoc.infra as aoc


@dataclass(frozen=True)
class Draw:
    red: int = 0
    green: int = 0
    blue: int = 0


def parse_draw(input: str) -> Draw:
    count_per_color: dict[str, int] = dict()
    for amount_and_color in input.split(","):
        amount, color = amount_and_color.strip().split()
        count_per_color[color] = int(amount)

    return Draw(**count_per_color)


@dataclass(frozen=True)
class Game:
    draws: list[Draw] = field(default_factory=list)


def parse_game(input: str) -> Game:
    draws = input.split(";")
    return Game(list(map(parse_draw, draws)))


def is_possible_draw(draw: Draw, bag: Draw) -> bool:
    return not any([draw.red > bag.red, draw.green > bag.green, draw.blue > bag.blue])


def is_possible_game(game: Game, bag: Draw) -> bool:
    return all([is_possible_draw(draw, bag) for draw in game.draws])


def possible_game_id(input: str, bag: Draw) -> int:
    front, draws = input.split(": ")
    game = parse_game(draws)

    if is_possible_game(game, bag):
        _, id = front.split()
        return int(id)

    return 0


def minimal_bag(game: Game, bag: Draw) -> Draw:
    observed_bag = Draw()
    for draw in game.draws:
        observed_bag = Draw(
            max(observed_bag.red, draw.red),
            max(observed_bag.green, draw.green),
            max(observed_bag.blue, draw.blue),
        )

    def min_without_zero(a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a
        return min(a, b)

    return Draw(
        min_without_zero(observed_bag.red, bag.red),
        min_without_zero(observed_bag.green, bag.green),
        min_without_zero(observed_bag.blue, bag.blue),
    )


def power(draw: Draw) -> int:
    return draw.red * draw.green * draw.blue


def solve_part_a(inputs: list[str], bag: Draw) -> int:
    return sum([possible_game_id(input, bag) for input in inputs])


def solve_part_b(inputs: list[str], bag: Draw) -> int:
    bag_powers: list[int] = list()
    for input in inputs:
        _, draws = input.split(": ")
        bag_powers.append(power(minimal_bag(parse_game(draws), bag)))

    return sum(bag_powers)


def main(
    part: str, red: int = 0, green: int = 0, blue: int = 0, submit: bool = False
) -> None:
    p = aoc.Part(part)
    bag = Draw(red, green, blue)

    inputs = aocd.get_data(day=2, year=aoc.YEAR).split("\n")

    solvers = {aoc.Part.A: solve_part_a, aoc.Part.B: solve_part_b}

    if submit:
        aocd.submit(solvers.get(p)(inputs, bag), p.value, day=2, year=aoc.YEAR)
    else:
        typer.echo(f"Result: {solvers.get(p)(inputs, bag)}")


if __name__ == "__main__":
    typer.run(main)
