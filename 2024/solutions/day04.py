import aocd
import typer

def part1() -> None:
    ...

def process_data(input: str) -> list[list[str]]:
    return list(map(str.split, input.split("\n")))
