from io import TextIOWrapper
from typing import NamedTuple


class Range(NamedTuple):
    lower:int
    upper:int


def parse_input(file_handle:TextIOWrapper) -> tuple[list[Range],list[int]]:
    ranges:list[Range] = []
    ingredients:list[int] = []
    lines = (l.strip() for l in file_handle.readlines())
    for line in lines:
        if not line:
            break
        ranges.append(Range(*map(int, line.split('-'))))
    for line in lines:
        ingredients.append(int(line))
    return ranges,ingredients


def part1(problem_input:tuple[list[Range],list[int]]) -> int:
    ranges,ingredients = problem_input
    return sum(any(lower<=ingredient<=upper for lower,upper in ranges) for ingredient in ingredients)


def part2(problem_input:tuple[list[Range],list[int]]) -> int:
    ranges,_ = problem_input
    ranges.sort()
    while True:
        merged_ranges:list[Range] = []
        a = ranges[0]
        for b in ranges[1:]:
            if a.upper>=b.lower:
                a = Range(a.lower,max(a.upper,b.upper))
            else:
                merged_ranges.append(a)
                a = b
        merged_ranges.append(a)
        if len(merged_ranges) == len(ranges):
            break
        ranges = merged_ranges
    return sum(r.upper-r.lower+1 for r in ranges)
