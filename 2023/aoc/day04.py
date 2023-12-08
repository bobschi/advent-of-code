import typer

from aoc.infra import get_cli


def winning_numbers(card: str) -> list[int]:
    winning_numbers, guessed_numbers = card.split("|")
    winning_numbers = set(map(int, winning_numbers.split()))
    guessed_numbers = set(map(int, guessed_numbers.split()))

    return list(sorted(guessed_numbers & winning_numbers))


def score(card: str) -> int:
    _, card = card.split(": ")
    cards_winning_numbers = winning_numbers(card)
    if len(cards_winning_numbers) > 0:
        return 2 ** (len(cards_winning_numbers) - 1)
    else:
        return 0


def solve_part_a(cards: list[str]) -> int:
    return sum(map(score, cards))


if __name__ == "__main__":
    typer.run(get_cli(solve_part_a, None, 4))
