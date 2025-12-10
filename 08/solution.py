from io import TextIOWrapper
from typing import Self

from functools import reduce
from itertools import combinations
from operator import mul


class CoordinateXYZ:
    x:int
    y:int
    z:int
    def __init__(self, x:int, y:int, z:int) -> None:
        self.x = x
        self.y = y
        self.z = z
    def __str__(self) -> str:
        return f'({self.x},{self.y},{self.z})'
    def __add__(self, other:Self) -> Self:
        return self.__class__(self.x+other.x, self.y+other.y, self.z+other.z)
    def __sub__(self, other:Self) -> Self:
        return self.__class__(self.x-other.x, self.y-other.y, self.z-other.z)
    def __abs__(self) -> int:
        return self.x**2+self.y**2+self.z**2
    def __hash__(self) -> int:
        return hash((self.x,self.y,self.z))


def parse_input(file_handle:TextIOWrapper) -> list[CoordinateXYZ]:
    return [CoordinateXYZ(*map(int, line.strip().split(','))) for line in file_handle.readlines()]


def connect_boxes(boxes:list[CoordinateXYZ], max_iterations:int=0) -> tuple[set[frozenset[CoordinateXYZ]],CoordinateXYZ,CoordinateXYZ]:
    circuits:dict[CoordinateXYZ,frozenset[CoordinateXYZ]] = {p:frozenset([p]) for p in boxes}
    distances:list[tuple[int,CoordinateXYZ,CoordinateXYZ]] = sorted((abs(a-b),a,b) for a,b in combinations(circuits.keys(), 2))
    if max_iterations>0:
        distances = distances[:max_iterations]
    for _,a,b in distances:
        c = circuits[a]|circuits[b]
        for d in circuits[a]:
            circuits[d] = c
        for d in circuits[b]:
            circuits[d] = c
        if len(c)==len(circuits):
            break
    return set(circuits.values()),a,b


def part1(problem_input:list[CoordinateXYZ]) -> int:
    iterations = 10 if len(problem_input)<1000 else 1000
    circuits,*_ = connect_boxes(problem_input, max_iterations=iterations)
    largest_circuits = sorted(circuits, key=lambda c: len(c))[-3::]
    return reduce(mul, (len(c) for c in largest_circuits))


def part2(problem_input:list[CoordinateXYZ]) -> int:
    _,a,b = connect_boxes(problem_input)
    return a.x*b.x
