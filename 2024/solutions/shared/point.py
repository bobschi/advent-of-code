from __future__ import annotations

class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def scalar_mult(self, factor: int) -> Point:
        return Point(self.x * factor, self.y * factor)

    def __repr__(self)->str:
        return f"({self.x},{self.y})"

    def __hash__(self) -> int:
        return hash((self.x, self.y))
    