"""
Day 2: Rock Paper Scissors
https://adventofcode.com/2022/day/2

Usage:
$ python solution.py [<file.txt>]
"""

import sys
from functools import cache
from pathlib import Path


def main(path: Path) -> None:
    """Load input data and assert the solution."""

    # Part 1
    assert 13005 == part1(load(path))

    # Part 2
    assert 11373 == part2(load(path))


def part1(moves: list[str]) -> int:
    return get_total_score(moves, points={
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    })


def part2(moves: list[str]) -> int:
    return get_total_score(moves, points={
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    })


def get_total_score(moves: list[str], points: dict[str, int]) -> int:
    """Return the total score of the game."""
    return sum(points[move] for move in moves)


@cache
def load(path: Path) -> list[str]:
    """Return a list of moves.

    Sample output:
    [
        "A Y",
        "B X",
        "C Z",
    ]
    """
    return path.read_text(encoding="utf-8").splitlines()


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path("input.txt"))
