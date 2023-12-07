import re
import enum
import aocd
import aoc.infra as aoc
import typer


class Position(enum.IntEnum):
    FIRST = 0
    LAST = -1


WORD_TO_DIGIT = dict(
    one="1",
    two="2",
    three="3",
    four="4",
    five="5",
    six="6",
    seven="7",
    eight="8",
    nine="9",
)


def part_specific_regex(part: aoc.Part) -> str:
    regexes = {
        aoc.Part.A: r"\d",
        aoc.Part.B: rf"(?=({'|'.join(WORD_TO_DIGIT.keys())}|\d))",
    }
    return regexes.get(part)


def digit(input: str, position: Position, part: aoc.Part) -> str:
    result: str = re.findall(part_specific_regex(part), input)[position.value]

    if not result.isdigit():
        return WORD_TO_DIGIT.get(result)

    return result


def calibration_value(input: str, part: aoc.Part) -> int:
    return int(digit(input, Position.FIRST, part) + digit(input, Position.LAST, part))


def solve(input: list[str], part: aoc.Part) -> int:
    return sum(map(calibration_value, input, part * len(input)))


def main(part: str, submit: bool = False) -> None:
    part = aoc.Part(part)
    inputs = aocd.get_data(day=1, year=2023).split("\n")
    result = solve(inputs, part)
    if submit:
        aocd.submit(result, part.value, day=1, year=2023)
    else:
        typer.echo(f"Result: {result}")


if __name__ == "__main__":
    typer.run(main)
