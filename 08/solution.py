from io import TextIOWrapper
from typing import NamedTuple,Self

from functools import reduce
from itertools import combinations
from operator import mul


class Point(NamedTuple):
    x:int
    y:int
    z:int
    def __sub__(self, other:Self) -> Self:
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)
    def __abs__(self) -> int:
        return self.x**2+self.y**2+self.z**2


def parse_input(file_handle:TextIOWrapper) -> list[Point]:
    return [Point(*map(int, line.strip().split(','))) for line in file_handle.readlines()]


def connect_boxes(boxes, max_iterations=0):
    circuits = {p:frozenset([p]) for p in boxes}
    distances = sorted((abs(a-b),a,b) for a,b in combinations(circuits.keys(), 2))
    if max_iterations>0:
        distances = distances[:max_iterations]
    for d,a,b in distances:
        c = circuits[a]|circuits[b]
        for d in circuits[a]:
            circuits[d] = c
        for d in circuits[b]:
            circuits[d] = c
        if len(c)==len(circuits):
            break
    return set(circuits.values()),a,b


def part1(problem_input:list[Point]) -> int:
    iterations = 10 if len(problem_input)<1000 else 1000
    circuits,*_ = connect_boxes(problem_input, max_iterations=iterations)
    largest_circuits = sorted(circuits, key=lambda c: len(c))[-3::]
    return reduce(mul, (len(c) for c in largest_circuits))


def part2(problem_input:list[Point]) -> int:
    _,a,b = connect_boxes(problem_input)
    return a.x*b.x
