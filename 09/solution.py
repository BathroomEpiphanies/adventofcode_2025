from io import TextIOWrapper
from typing import Self

from itertools import combinations, pairwise


class CoordinateXY:
    x:int
    y:int
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f'({self.x},{self.y})'
    def __add__(self, other:Self) -> Self:
        return self.__class__(self.x+other.x, self.y+other.y)
    def __sub__(self, other:Self) -> Self:
        return self.__class__(self.x-other.x, self.y-other.y)
    def __abs__(self) -> int:
        return self.x**2+self.y**2
    def __hash__(self) -> int:
        return hash((self.x,self.y))


def parse_input(file_handle:TextIOWrapper) -> list[CoordinateXY]:
    tiles = []
    for line in file_handle.readlines():
        a,b = line.strip().split(',')
        tiles.append(CoordinateXY(int(a), int(b)))
    return tiles


def part1(problem_input:list[CoordinateXY]) -> int:
    return max((abs(a.x-b.x)+1)*(abs(a.y-b.y)+1) for a,b in combinations(problem_input, 2))


def part2(problem_input:list[CoordinateXY]) -> int:
    largest = 0
    segments = [(a,b) for a,b in pairwise(problem_input)]
    for tile1,tile2 in combinations(problem_input, 2):
        left = min(tile1.x, tile2.x)
        right = max(tile1.x, tile2.x)
        top = min(tile1.y, tile2.y)
        bottom = max(tile1.y, tile2.y)
        for s1,s2 in segments:
            if {s1,s2}&{tile1,tile2}:
                continue
            l = min(s1.x, s2.x)
            r = max(s1.x, s2.x)
            t = min(s1.y, s2.y)
            b = max(s1.y, s2.y)
            if t==b and top<t<bottom:
                if left<l<right or left<r<right or l<=left and r>=right:
                    break
            if l==r and left<l<right:
                if top<t<bottom or top<b<bottom or t<=top and b>=bottom:
                    break
        else:
            size = (abs(tile1.x-tile2.x)+1)*(abs(tile1.y-tile2.y)+1)
            if size>=largest:
                largest = size 
                #print(size, tile1, tile2)
    return largest
