from dataclasses import dataclass

import typer

from aoc.infra import get_cli


@dataclass
class Card:
    id: int
    winners: list[int]
    guesses: list[int]
    count: int = 1


def parse_card(line: str) -> Card:
    card_id, winners_and_guesses = line.split(": ")
    _, id = card_id.split()
    winners, guesses = winners_and_guesses.split("|")

    id = int(id)
    winners = list(map(int, winners.split()))
    guesses = list(map(int, guesses.split()))

    return Card(id, winners, guesses)


def winning_numbers(card: Card) -> list[int]:
    return list(sorted(set(card.guesses) & set(card.winners)))


def score(card: Card) -> int:
    cards_winning_numbers = winning_numbers(card)
    if len(cards_winning_numbers) > 0:
        return 2 ** (len(cards_winning_numbers) - 1)
    else:
        return 0


def solve_part_a(cards: list[str]) -> int:
    return sum(map(score, map(parse_card, cards)))


def generate_copies(cards: list[Card]) -> None:
    for card in cards:
        number_winners = len(winning_numbers(card))
        for to_increase in range(card.id, card.id + number_winners):
            if to_increase < len(cards):
                cards[to_increase].count += card.count


def solve_part_b(input: list[str]) -> int:
    cards = list(map(parse_card, input))
    generate_copies(cards)

    return sum([card.count for card in cards])


if __name__ == "__main__":
    typer.run(get_cli(solve_part_a, solve_part_b, 4))
