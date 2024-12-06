import pytest


@pytest.fixture
def example_input() -> str:
    return (
        "....#....."
        ".........#"
        ".........."
        "..#......."
        ".......#.."
        ".........."
        ".#..^....."
        "........#."
        "#........."
        "......#..."
    )
