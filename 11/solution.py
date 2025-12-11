from io import TextIOWrapper

from functools import cache


def parse_input(file_handle:TextIOWrapper) -> dict[str,list[str]]:
    edges:dict[str,list[str]] = {}
    for line in file_handle.readlines():
        source,targets_ = line.strip().split(': ')
        targets = targets_.split(' ')
        edges[source] = targets
    return edges


def count_paths(edges:dict[str,list[str]], source:str, sink:str, dac:bool=True, fft:bool=True) -> int:
    @cache
    def __count_paths(S:str, T:str, dac:bool, fft:bool) -> int:
        if S==T:
            return 1 if dac and fft else 0
        else:
            return sum(__count_paths(s, T, dac or S=='dac', fft or S=='fft') for s in edges[S])
    return __count_paths(source, sink, dac, fft)


def part1(problem_input:dict[str,list[str]]) -> int:
    return count_paths(problem_input, 'you', 'out')


def part2(problem_input:dict[str,list[str]]) -> int:
    return count_paths(problem_input, 'svr', 'out', dac=False, fft=False)
