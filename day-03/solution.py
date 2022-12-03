"""
Day 3: Rucksack Reorganization
https://adventofcode.com/2022/day/3

Usage:
$ python solution.py [<file.txt>]
"""
import string
import sys
from functools import cache
from pathlib import Path
from typing import Iterable


def main(path: Path) -> None:
    """Load input data and assert the solution."""

    # Part 1
    assert 7980 == part1(load(path))

    # Part 2
    assert 2881 == part2(load(path))


def part1(rucksacks: list[str]) -> int:
    return sum(get_priority(find_common_item(r)) for r in rucksacks)


def part2(rucksacks: list[str]) -> int:
    return sum(get_priority(find_badge(g)) for g in grouper(rucksacks, 3))


def find_common_item(rucksack: str) -> str:
    middle = len(rucksack) // 2
    left, right = rucksack[:middle], rucksack[middle:]
    return next(iter(set(left) & set(right)))


def get_priority(item: str) -> int:
    return string.ascii_letters.index(item) + 1


def grouper(rucksacks: list[str], group_size: int) -> Iterable[set[str]]:
    for i in range(0, len(rucksacks), group_size):
        yield map(set, rucksacks[i: i + group_size])


def find_badge(group: set[str]) -> str:
    return next(iter(set.intersection(*group)))


@cache
def load(path: Path) -> list[str]:
    """Return a list of rucksacks.

    Sample output:
    [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    """
    return path.read_text(encoding="utf-8").splitlines()


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path("input.txt"))
