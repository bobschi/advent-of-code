import aocd
import typer
import re

app = typer.Typer()


@app.command()
def part1() -> None:
    data = aocd.get_data(day=3, year=2024)
    muls = re.compile(r"mul\(\d+\,\d+\)")
    instructions = (muls.findall(line) for line in data)
    numbers = (
        tuple(map(int, re.compile(r"\d+").findall(instruction)))
        for instruction_set in instructions
        for instruction in instruction_set
    )
    solution=sum((mul[0]*mul[1] for mul in numbers))
    aocd.submit(answer=solution,part="a",day=3,year=2024)


@app.command()
def part2() -> None:
    data = aocd.get_data(day=3, year=2024)
    instructions=re.compile(r"mul\(\d+\,\d+\)|don't\(\)|do\(\)")
    enabled = True
    solution = 0
    for instruction in instructions.findall(data):
        if(re.compile(r"mul\(\d+\,\d+\)").match(instruction)):
            nums = tuple(map(int,re.compile(r"\d+").findall(instruction)))
            if enabled:
                solution = solution + nums[0]*nums[1]
        if re.compile(r"do\(\)").fullmatch(instruction):
            enabled = True
        if re.compile(r"don't\(\)").fullmatch(instruction):
            enabled = False
    aocd.submit(answer=solution,part="b",day=3,year=2024)

