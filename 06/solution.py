from io import TextIOWrapper
from typing import Callable
from functools import reduce
from operator import add,mul


class Expression:
    operands:list[str]
    operator:Callable[[int,int],int]
    
    def __init__(self, operands:list[str], operator:str) -> None:
        self.operands = operands
        self.operator = {'+':add,'*':mul}[operator]
    
    def human_value(self) -> int:
        return reduce(self.operator, (int(''.join(r)) for r in self.operands))
    
    def cephalopod_value(self) -> int:
        return reduce(self.operator, (int(''.join(r)) for r in zip(*self.operands)))


def parse_input(file_handle:TextIOWrapper) -> list[Expression]:
    math_sheet = [l.strip('\n')+' ' for l in file_handle.readlines()]
    expressions:list[Expression] = []
    i = 0
    for c,_ in enumerate(math_sheet[0]):
        if all(row[c]==' ' for row in math_sheet):
            operands = [row[i:c] for row in math_sheet[:-1]]
            operator = math_sheet[-1][i:c].strip()
            expressions.append(Expression(operands, operator))
            i = c+1
    return expressions


def part1(problem_input:list[Expression]) -> int:
    return sum(expression.human_value() for expression in problem_input)


def part2(problem_input:list[Expression]) -> int:
    return sum(expression.cephalopod_value() for expression in problem_input)