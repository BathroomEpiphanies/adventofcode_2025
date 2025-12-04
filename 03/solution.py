from io import TextIOWrapper


def parse_input(file_handle:TextIOWrapper) -> list[list[int]]:
    return [[int(n) for n in line.strip()] for line in file_handle.readlines()]


def largest_bank_joltage(bank:list[int], n:int) -> int:
    if n==1:
        return max(bank)
    m = max(bank[:-(n-1)])
    i = bank.index(m)
    return m*10**(n-1) + largest_bank_joltage(bank[i+1:], n-1)


def part1(problem_input:list[list[int]]) -> int:
    return sum(largest_bank_joltage(bank, 2) for bank in problem_input)


def part2(problem_input:list[list[int]]) -> int:
    return sum(largest_bank_joltage(bank, 12) for bank in problem_input)
