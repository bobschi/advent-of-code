from itertools import pairwise

import typer

from aoc.infra import get_cli


def parse_history(history: str) -> list[int]:
    return list(map(int, history.split()))


def get_differences(sequence: list[int]) -> list[int]:
    return [b - a for a, b in pairwise(sequence)]


def get_last_element(sequence: list[int]) -> int:
    return sequence[-1]


def setup_prediction(sequence: list[int]) -> list[int]:
    current_difference = get_differences(sequence)
    differences = [sequence, current_difference]
    while not all(n == 0 for n in current_difference):
        current_difference = get_differences(current_difference)
        differences.append(current_difference)

    return list(map(get_last_element, differences))


def predict(sequence: list[int]) -> int:
    last_differences = sorted(setup_prediction(sequence))
    new_last_elements = [0]
    for difference in last_differences:
        new_last_element = difference + get_last_element(new_last_elements)
        new_last_elements.append(new_last_element)

    return get_last_element(new_last_elements)


def solve_part_a(inputs: list[str]) -> int:
    histories = list(map(parse_history, inputs))
    predictions = list(map(predict, histories))

    return sum(predictions)


def solve_part_b(inputs: list[str]) -> int:
    histories = list(map(parse_history, inputs))
    for history in histories:
        history.reverse()
    predictions = list(map(predict, histories))

    return sum(predictions)


if __name__ == "__main__":
    typer.run(get_cli(solve_part_a, solve_part_b, 9))
