import pytest

from solutions.day05 import (
    Rule,
    RulesAndUpdates,
    Update,
    fix_order,
    is_correctly_ordered,
    is_relevant,
    is_satisfied,
    middle_number,
    printable_updates,
    process_data,
)


@pytest.fixture
def sample_input() -> str:
    return (
        "47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n"
        "97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n"
        "75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n"
        "97,13,75,29,47"
    )


@pytest.fixture
def processed_input(sample_input: str) -> RulesAndUpdates:
    return process_data(sample_input)


@pytest.fixture
def inccorectly_ordered(processed_input: RulesAndUpdates) -> RulesAndUpdates:
    rules, updates = processed_input
    inccorectly_ordered = [u for u in updates if not is_correctly_ordered(u, rules)]
    return (rules, inccorectly_ordered)


def test_process_data(sample_input: str) -> None:
    rules, manuals = process_data(sample_input)

    assert Rule(47, 53) in rules
    assert Rule(75, 47) in rules
    assert len(rules) == 21

    assert Update([75, 29, 13]) in manuals
    assert Update([97, 13, 75, 29, 47]) in manuals
    assert len(manuals) == 6


def test_is_relevant(processed_input: RulesAndUpdates) -> None:
    _, manuals = processed_input

    assert is_relevant(Rule(75, 47), manuals[0])
    assert not is_relevant(Rule(75, 47), manuals[1])
    assert not is_relevant(Rule(75, 47), manuals[2])
    assert is_relevant(Rule(75, 47), manuals[3])
    assert not is_relevant(Rule(75, 47), manuals[4])
    assert is_relevant(Rule(75, 47), manuals[3])


def test_is_satisfied(processed_input: RulesAndUpdates) -> None:
    _, manuals = processed_input

    assert is_satisfied(Rule(75, 47), manuals[0])
    assert not is_satisfied(Rule(75, 47), manuals[1])
    assert not is_satisfied(Rule(75, 47), manuals[2])
    assert is_satisfied(Rule(75, 47), manuals[3])
    assert not is_satisfied(Rule(75, 47), manuals[4])
    assert is_satisfied(Rule(75, 47), manuals[3])


def test_middle_number(processed_input: RulesAndUpdates) -> None:
    _, manuals = processed_input

    assert middle_number(manuals[0]) == 61
    assert middle_number(manuals[1]) == 53
    assert middle_number(manuals[2]) == 29
    assert middle_number(manuals[3]) == 47
    assert middle_number(manuals[4]) == 13
    assert middle_number(manuals[5]) == 75


def test_printable_manuals(processed_input: RulesAndUpdates) -> None:
    rules, updates = processed_input

    expected = [
        Update([75, 47, 61, 53, 29]),
        Update([97, 61, 53, 29, 13]),
        Update([75, 29, 13]),
    ]

    assert printable_updates(rules, updates) == expected


def test_update_swap_at() -> None:
    under_test = Update([1, 2, 3, 4, 5, 6])
    expected = Update([1, 3, 2, 4, 5, 6])

    under_test.swap_at(1,2)

    assert under_test == expected


def test_fix_order(inccorectly_ordered: RulesAndUpdates) -> None:
    rules, updates = inccorectly_ordered
    expected_0 = Update([97, 75, 47, 61, 53])
    expected_1 = Update([61, 29, 13])
    expected_2 = Update([97, 75, 47, 29, 13])

    for update in updates:
        fix_order(update, rules)

    assert updates[0] == expected_0
    assert updates[1] == expected_1
    assert updates[2] == expected_2
