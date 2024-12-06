from __future__ import annotations

from enum import Enum

from solutions.shared import Point


class Dir(Enum):
    N = Point(-1, 0)
    NE = Point(-1, 1)
    E = Point(0, 1)
    SE = Point(1, 1)
    S = Point(1, 0)
    SW = Point(1, -1)
    W = Point(0, -1)
    NW = Point(-1, -1)

    @staticmethod
    def all() -> list[Dir]:
        return [Dir.N, Dir.NE, Dir.E, Dir.SE, Dir.S, Dir.SW, Dir.W, Dir.NW]
    
    @staticmethod
    def cardinals() -> list[Dir]:
        return [Dir.N, Dir.E, Dir.S, Dir.W]
