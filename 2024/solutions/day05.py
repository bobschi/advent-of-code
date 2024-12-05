from __future__ import annotations

import aocd
import typer
from rich.progress import track
from collections import defaultdict

app = typer.Typer()


class Rule:
    a: int
    b: int

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def __eq__(self, other) -> bool:
        return self.a == other.a and self.b == other.b

    def __repr__(self) -> str:
        return f"{self.a} < {self.b}"

    def as_set(self) -> set[int]:
        return {self.a, self.b}


class Update:
    pages: list[int]

    def __init__(self, pages: list[int]) -> None:
        self.pages = pages

    def __eq__(self, other) -> bool:
        return self.pages == other.pages

    def index(self, item: int) -> int:
        return self.pages.index(item)

    def swap_at(self, a: int, b: int) -> None:
        self.pages[a], self.pages[b] = self.pages[b], self.pages[a]

    def __repr__(self) -> str:
        return str(self.pages)


type RulesAndUpdates = tuple[list[Rule], list[Update]]
type Rules = list[Rule]
type Updates = list[Update]


def is_relevant(rule: Rule, update: Update) -> bool:
    return rule.a in update.pages and rule.b in update.pages


def is_satisfied(rule: Rule, update: Update) -> bool:
    return is_relevant(rule, update) and update.index(rule.a) < update.index(rule.b)


def middle_number(update: Update) -> int:
    return update.pages[len(update.pages) // 2]


def is_correctly_ordered(update: Update, rules: Rules) -> bool:
    applicable_rules = list([rule for rule in rules if is_relevant(rule, update)])
    return all([is_satisfied(rule, update) for rule in applicable_rules])


def printable_updates(rules: Rules, updates: Updates) -> Updates:
    return [update for update in updates if is_correctly_ordered(update, rules)]


def process_data(input: str) -> RulesAndUpdates:
    rules: list[Rule] = []
    updates: list[Update] = []
    for line in input.split("\n"):
        if "|" in line:
            rules.append(Rule(*list(map(int, line.split("|")))))
        elif "," in line:
            updates.append(Update(list(map(int, line.split(",")))))
    return (rules, updates)


@app.command()
def part1() -> None:
    rules, updates = process_data(aocd.get_data(day=5, year=2024))
    valid_updates = printable_updates(rules, updates)
    aocd.submit(str(sum(map(middle_number, valid_updates))), part="a", day=5, year=2024)


def rules_to_fix(update: Update, rules: Rules) -> Rules:
    return [r for r in rules if not is_satisfied(r, update) and is_relevant(r, update)]


def fix_order(update: Update, rules: Rules) -> None:
    numbers_after = defaultdict(list)
    for rule in rules:
        numbers_after[rule.a].append(rule.b)

    while not is_correctly_ordered(update, rules):
        for key in reversed(numbers_after.keys()):
            if key not in update.pages:
                continue

            while any(
                [na in update.pages[: update.index(key)] for na in numbers_after[key]]
            ):
                index = update.index(key)
                update.swap_at(index - 1, index)


@app.command()
def part2() -> None:
    rules, updates = process_data(aocd.get_data(day=5, year=2024))
    incorrectly_ordered = [u for u in updates if not is_correctly_ordered(u, rules)]
    for update in track(incorrectly_ordered):
        fix_order(update, rules)

    aocd.submit(
        str(sum(map(middle_number, incorrectly_ordered))), part="b", day=5, year=2024
    )
