from io import TextIOWrapper

import z3


class Machine:
    buttons:list[list[int]]
    indicators:list[int]
    joltages:list[int]
    def __init__(self, description:str) -> None:
        tokens = description.split(' ')
        self.indicators = [{'.':0, '#':1}[i] for i in tokens[0][1:-1]]
        self.joltages = [int(j) for j in tokens[-1][1:-1].split(',')]
        self.buttons = [
            [int(j) for j in token[1:-1].split(',')]
            for token in tokens[1:-1]
        ]
    def __str__(self) -> str:
        return f'[{self.indicators}] ({self.buttons}) {{{self.joltages}}}'


def parse_input(file_handle:TextIOWrapper) -> list[Machine]:
    return [Machine(line.strip()) for line in file_handle.readlines()]


def minimize_presses(targets:list[int], buttons:list[list[int]], mod:int=0) -> int:
    optimizer = z3.Optimize()
    ns = [z3.Int(f'n{i}') for i,_ in enumerate(buttons)]
    js:list[list[z3.Int]] = [[] for _ in targets]
    for ni,button in zip(ns, buttons):
        optimizer.add(ni>=0)
        for b in button:
            js[b].append(ni)
    for ji,ti in zip(js, targets):
        if mod:
            optimizer.add(sum(ji)%mod==ti)
        else:
            optimizer.add(sum(ji)==ti)
    N = z3.Int('N')
    optimizer.add(N==sum(ns))
    optimizer.minimize(N)
    optimizer.check()
    return int(optimizer.model()[N].as_long())


def part1(problem_input:list[Machine]) -> int:
    return sum(minimize_presses(m.indicators, m.buttons, mod=2) for m in problem_input)


def part2(problem_input:list[Machine]) -> int:
    return sum(minimize_presses(m.joltages, m.buttons) for m in problem_input)
