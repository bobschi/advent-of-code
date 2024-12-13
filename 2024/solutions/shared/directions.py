from __future__ import annotations

from enum import Enum

from solutions.shared import Vector


class Dir(Enum):
    N = Vector(-1, 0)
    NE = Vector(-1, 1)
    E = Vector(0, 1)
    SE = Vector(1, 1)
    S = Vector(1, 0)
    SW = Vector(1, -1)
    W = Vector(0, -1)
    NW = Vector(-1, -1)

    @staticmethod
    def all() -> list[Dir]:
        return [Dir.N, Dir.NE, Dir.E, Dir.SE, Dir.S, Dir.SW, Dir.W, Dir.NW]
    
    @staticmethod
    def cardinals() -> list[Dir]:
        return [Dir.N, Dir.E, Dir.S, Dir.W]
