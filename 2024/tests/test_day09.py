import pytest

from solutions.day09 import (
    File,
    FileStream,
    FreeSpace,
    IdList,
    checksum,
    defrag,
    file_defrag,
    process_data,
)


@pytest.fixture
def example_input_1() -> str:
    return "2333133121414131402"


@pytest.fixture
def example_file_stream_1() -> FileStream:
    return [
        File(id=0, length=2),
        FreeSpace(length=3),
        File(id=1, length=3),
        FreeSpace(length=3),
        File(id=2, length=1),
        FreeSpace(length=3),
        File(id=3, length=3),
        FreeSpace(length=1),
        File(id=4, length=2),
        FreeSpace(length=1),
        File(id=5, length=4),
        FreeSpace(length=1),
        File(id=6, length=4),
        FreeSpace(length=1),
        File(id=7, length=3),
        FreeSpace(length=1),
        File(id=8, length=4),
        FreeSpace(length=0),
        File(id=9, length=2),
    ]


@pytest.fixture
def example_id_list_1() -> IdList:
    return [
        0,
        0,
        9,
        9,
        8,
        1,
        1,
        1,
        8,
        8,
        8,
        2,
        7,
        7,
        7,
        3,
        3,
        3,
        6,
        4,
        4,
        6,
        5,
        5,
        5,
        5,
        6,
        6,
        *(-1 for _ in range(14)),
    ]


@pytest.fixture
def example_id_list_file_defrag_1() -> IdList:
    return [
        0,
        0,
        9,
        9,
        2,
        1,
        1,
        1,
        7,
        7,
        7,
        -1,
        4,
        4,
        -1,
        3,
        3,
        3,
        -1,
        -1,
        -1,
        -1,
        5,
        5,
        5,
        5,
        -1,
        6,
        6,
        6,
        6,
        -1,
        -1,
        -1,
        -1,
        -1,
        8,
        8,
        8,
        8,
        -1,
        -1,
    ]


@pytest.fixture
def example_input_2() -> str:
    return "12345"


@pytest.fixture
def example_file_stream_2() -> FileStream:
    return [
        File(id=0, length=1),
        FreeSpace(length=2),
        File(id=1, length=3),
        FreeSpace(length=4),
        File(id=2, length=5),
    ]


@pytest.fixture
def example_id_list_2() -> IdList:
    return [0, 2, 2, 1, 1, 1, 2, 2, 2, -1, -1, -1, -1, -1, -1]


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        ["example_input_1", "example_file_stream_1"],
        ["example_input_2", "example_file_stream_2"],
    ],
)
def test_process_data(input: str, expected: str, request) -> None:
    example_input = request.getfixturevalue(input)
    expected_output = request.getfixturevalue(expected)
    assert process_data(example_input) == expected_output


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        ["example_file_stream_1", "example_id_list_1"],
        ["example_file_stream_2", "example_id_list_2"],
    ],
)
def test_defrag(input: str, expected: str, request) -> None:
    example_input = request.getfixturevalue(input)
    expected_output = request.getfixturevalue(expected)
    assert defrag(example_input) == expected_output


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        ["example_id_list_1", 1928],
        ["example_id_list_2", 60],
    ],
)
def test_checksum(input: str, expected: int, request) -> None:
    example_input = request.getfixturevalue(input)
    assert checksum(example_input) == expected


def test_file_defrag(
    example_file_stream_1: FileStream, example_id_list_file_defrag_1: IdList
) -> None:
    assert file_defrag(example_file_stream_1) == example_id_list_file_defrag_1
