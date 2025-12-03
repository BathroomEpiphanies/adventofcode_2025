from io import TextIOWrapper
from more_itertools import all_equal, grouper


def parse_input(file_handle:TextIOWrapper) -> list[tuple[int,int]]:
    ranges:list[tuple[int,int]] = []
    for range in file_handle.readline().split(','):
        start,stop = range.strip().split('-')
        ranges.append((int(start),int(stop)))
    return ranges


def part1(problem_input:list[tuple[int,int]]) -> int:
    def check_id(id_:int) -> bool:
        id_string = str(id_)
        l = len(id_string)
        return id_string[:l//2] != id_string[l//2:]
    
    invalid_id_sum:int = 0
    for start,stop in problem_input:
        for id_ in range(start,stop+1):
            if not check_id(id_):
                invalid_id_sum += id_
    return invalid_id_sum


def part2(problem_input:list[tuple[int,int]]) -> int:
    def check_id(id_:int) -> bool:
        id_string = str(id_)
        for l in range(1,len(id_string)//2+1):
            if all_equal(grouper(id_string, l, incomplete='fill', fillvalue=' ')):
                return False
        return True
    
    invalid_id_sum:int = 0
    for start,stop in problem_input:
        for id_ in range(start,stop+1):
            if not check_id(id_):
                invalid_id_sum += id_
    return invalid_id_sum
