from adventofcode.util.input_helpers import get_test_input_for_day
from adventofcode.year_2022.day_04_2022 import part_two, part_one


def test_part_one():
    answer = part_one(get_test_input_for_day(2022, 4))
    assert answer == 2


def test_part_two():
    answer = part_two(get_test_input_for_day(2022, 4))
    assert answer ==4
