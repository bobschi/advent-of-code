from __future__ import annotations

from functools import partial
from math import log10

import aocd
import typer

app = typer.Typer()


class Equation:
    total: int
    operands: list[int]

    def __init__(self, numbers: list[int]) -> None:
        total, *operands = numbers
        self.total = total
        self.operands = operands

    def __eq__(self, other) -> bool:
        return self.total == other.total and self.operands == other.operands

    def __repr__(self) -> str:
        return f"{self.total} = {self.operands}"


type Equations = list[Equation]


def process_data(input: str) -> Equations:
    return [
        Equation(list(map(int, line.replace(":", "").split())))
        for line in input.split("\n")
    ]


def digits(number: int) -> int:
    return int(log10(number)) + 1


def ends_with(number: int, last_digit: int):
    return (number - last_digit) % 10 ** digits(last_digit) == 0


def solvable(equation: Equation, check_concat: bool = False) -> bool:
    def has_solution(test_value: int, numbers: list[int], check_concat: bool) -> bool:
        *head, number = numbers

        if not head:
            return number == test_value

        quotient, rest = divmod(test_value, number)
        if rest == 0 and has_solution(quotient, head, check_concat):
            return True

        if (
            check_concat
            and ends_with(test_value, number)
            and has_solution(test_value // (10 ** digits(number)), head, check_concat)
        ):
            return True

        return has_solution(test_value - number, head, check_concat)

    return has_solution(equation.total, equation.operands, check_concat)


@app.command()
def part1() -> None:
    data = aocd.get_data(day=7, year=2024)

    equations = process_data(data)
    solvable_equations = list(filter(solvable, equations))
    solution = sum([eq.total for eq in solvable_equations])

    aocd.submit(answer=str(solution), part="a", day=7, year=2024)


@app.command()
def part2() -> None:
    data = aocd.get_data(day=7, year=2024)

    equations = process_data(data)
    solvable_with_concat = partial(solvable, check_concat=True)
    solvable_equations = list(filter(solvable_with_concat, equations))
    solution = sum([eq.total for eq in solvable_equations])

    aocd.submit(answer=str(solution), part="b", day=7, year=2024)


if __name__ == "__main__":
    app()
