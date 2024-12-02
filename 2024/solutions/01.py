import aocd
import typer
from collections import Counter

app = typer.Typer()

def get_data() -> tuple[list[int],list[int]]:
    data = aocd.get_data(day=1, year=2024).split("\n")
    return map(sorted, zip(*(map(int, line.split()) for line in data)))


@app.command()
def part1() -> None:
    differences = [abs(a - b) for a, b in zip(get_data())]
    aocd.submit(answer=sum(differences), part="a", day=1, year=2024)


@app.command()
def part2() -> None:
    left,right = get_data()
    counts = Counter(right)
    similarity_scores = [number * counts[number] for number in left]
    aocd.submit(answer=sum(similarity_scores), part="b", day=1, year=2024)
