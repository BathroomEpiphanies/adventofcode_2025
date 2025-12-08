from io import TextIOWrapper
from functools import cache


def parse_input(file_handle:TextIOWrapper) -> tuple[complex,dict[complex,str]]:
    start:complex = 0
    manifold:dict[complex,str] = {}
    for r,row in enumerate(file_handle.readlines()):
        for c,content in enumerate(row.strip()):
            if content=='S':
                start = r*1j+c
            manifold[r*1j+c] = content
    return start,manifold


def part1(problem_input:tuple[int,dict[complex,str]]) -> int:
    start,manifold = problem_input
    found = set()
    def find_splitters(position:complex) -> int:
        if position in found or position not in manifold:
            return 0
        found.add(position)
        if manifold[position]=='^':
            return 1 + find_splitters(position-1) + find_splitters(position+1)
        else:
            return find_splitters(position+1j)
    return find_splitters(start)


def part2(problem_input:tuple[int,dict[complex,str]]) -> int:
    start,manifold = problem_input
    @cache
    def find_paths(position:complex) -> int:
        if position not in manifold:
            return 1
        elif manifold[position] == '^':
            return find_paths(position-1)+find_paths(position+1)
        else:
            return find_paths(position+1j)
    return find_paths(start)
