

def parse_input(file_handle) -> list[int]:
    return [-int(l[1:]) if l[0]=='L' else int(l[1:]) for l in file_handle.readlines()]


def part1(problem_input:list[int]) -> int:
    zero_count:int = 0
    position:int = 50
    for rotation in problem_input:
        position = (position+rotation)%100
        if position == 0:
            zero_count += 1
    return zero_count


def part2(problem_input:list[int]) -> int:
    zero_count:int = 0
    position:int = 50
    for rotation in problem_input:
        if rotation<0 and position!=0:
            position = position-100
        position += rotation
        zero_count += abs(position)//100
        position %= 100
    return zero_count
