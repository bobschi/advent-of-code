import enum
from typing import Callable

import aocd
import typer
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn

YEAR = 2023


class Part(enum.StrEnum):
    A = "a"
    B = "b"


Solver = Callable[[list[str]], int]

progress = Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    TimeElapsedColumn(),
    transient=True,
)


def get_cli(solver_a: Solver, solver_b: Solver | None, day: int):
    def cli(part: str, submit: bool = False):
        p = Part(part)
        inputs = aocd.get_data(day=day, year=YEAR).split("\n")

        with progress:
            progress.add_task(description="Solving ...", total=None)
            if p == Part.A:
                result = solver_a(inputs)
            elif solver_b is not None:
                result = solver_b(inputs)
            else:
                result = "No solver for part B"

        if submit:
            aocd.submit(result, p.value, day=day, year=YEAR)
        else:
            typer.echo(f"Result: {result}")

    return cli
