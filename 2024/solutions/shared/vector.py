from __future__ import annotations


class Vector:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def scalar_mult(self, factor: int) -> Vector:
        return Vector(self.x * factor, self.y * factor)

    def sqdist(self) -> int:
        return self.x * self.x + self.y * self.y

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __lt__(self, other: Vector) -> bool:
        return self.sqdist() < other.sqdist()

    def __gt__(self, other: Vector) -> bool:
        return self.sqdist() > other.sqdist()
