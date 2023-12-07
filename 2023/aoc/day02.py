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


def parse_game(input: str) -> Draw:
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


def solve_part_a(inputs: list[str], bag: Draw) -> int:
    return sum([possible_game_id(input, bag) for input in inputs])


def main(part: str, red: int, green: int, blue: int, submit: bool = False) -> None:
    day = 2

    part = aoc.Part(part)
    bag = Draw(red, green, blue)

    inputs = aocd.get_data(day=day, year=aoc.YEAR).split("\n")

    result = solve_part_a(inputs, bag)

    if submit:
        aocd.submit(result.value, day=day, year=aoc.YEAR)
    else:
        typer.echo(f"Result: {result}")


if __name__ == "__main__":
    typer.run(main)
