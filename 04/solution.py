from io import TextIOWrapper


def parse_input(file_handle:TextIOWrapper) -> set[complex]:
    roll_positions:set[complex] = set()
    for row,line in enumerate(file_handle.readlines()):
        for column,grid_content in enumerate(line.strip()):
            if grid_content=='@':
                roll_positions.add(column+row*1j)
    return roll_positions


directions = frozenset([+1+0j, +1+1j, +0+1j, -1+1j, -1+0j, -1-1j, +0-1j, +1-1j])


def part1(problem_input:set[complex]) -> int:
    return sum(
        sum(roll_position+direction in problem_input for direction in directions) < 4
        for roll_position in problem_input
    )


def part2(problem_input:set[complex]) -> int:
    removable_roll_count:int = 0
    while True:
        rolls_to_remove:set[complex] = set()
        for roll_position in problem_input:
            if sum(roll_position+direction in problem_input for direction in directions) < 4:
                rolls_to_remove.add(roll_position)
        if not rolls_to_remove:
            break
        problem_input -= rolls_to_remove
        removable_roll_count += len(rolls_to_remove)
    return removable_roll_count
