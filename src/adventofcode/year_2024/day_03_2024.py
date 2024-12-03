from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2024, 3, 1)
def part_one(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2024, 3, 1)

    return answer


@solution_timer(2024, 3, 2)
def part_two(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2024, 3, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2024, 3)
    part_one(data)
    part_two(data)