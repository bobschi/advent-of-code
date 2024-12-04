import pytest
from solutions import "04" as day4


@pytest.fixture
def example_input():
    return (
        "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\n"
        "SMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX"
    )


@pytest.fixture
def example_solution():
    return 18


def test_part1() -> None: ...

def test_process_data(example_input:str)->None:
    output = process_data(example_input)


