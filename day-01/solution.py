"""
Day 1: Calorie Counting
https://adventofcode.com/2022/day/1

Usage:
$ python solution.py [<file.txt>]
"""

import sys
from functools import cache
from pathlib import Path


def main(path: Path) -> None:
    """Load input data and assert the solution."""

    # Part 1
    assert 69795 == find_most_calories(load(path))

    # Part 2
    assert 208437 == find_top_three_elves(load(path))


@cache
def load(path: Path) -> list[int]:
    """Return a list of calories per elf.

    Sample output:
    [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]
    """
    puzzle_input = path.read_text(encoding="utf-8")
    return [
        sum(int(calories) for calories in elf.split("\n"))
        for elf in puzzle_input.split("\n\n")
    ]


def find_most_calories(calories: list[int]) -> int:
    """Return the maximum number of calories."""
    return max(calories)


def find_top_three_elves(calories: list[int]) -> int:
    """Return the top three elves."""
    return sum(sorted(calories)[-3:])


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path("input.txt"))
