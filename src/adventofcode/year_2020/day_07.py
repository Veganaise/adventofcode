import re
from typing import Tuple, List, Dict

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


bag_type_pattern = re.compile(r'^([a-z]+ [a-z]+)')
contents_pattern = re.compile(r'((\d) ([a-z]+ [a-z]+))')
gold_bag = 'shiny gold'


@solution_timer(2020, 7, 1)
def part_one(input_data: List[str]) -> int:
    bags = get_bags(input_data)
    gold_holders = []
    for bag in bags:
        if search(bags, bag, gold_bag):
            gold_holders.append(bag)

    return len(gold_holders)


@solution_timer(2020, 7, 2)
def part_two(input_data: List[str]) -> int:
    bags = get_bags(input_data)
    return bag_counter(gold_bag, bags, 1, 0)


def get_bags(input_data: List[str]) -> Dict[str, Dict[str, int]]:
    bags = {}

    for line in input_data:
        bag = bag_type_pattern.match(line).group()
        contents = contents_pattern.findall(line)
        bags[bag] = {}

        for content in contents:
            _, number_str, _bag = content
            bags[bag][_bag] = int(number_str)

    return bags


def search(bags: Dict[str, Dict[str, int]], current_bag: str, bag: str) -> bool:
    contents = [content for content in bags[current_bag].keys()]
    if contents:
        for content in contents:
            if content == bag:
                return True
            else:
                if search(bags, content, bag):
                    return True
    else:
        return False


def bag_counter(bag: str, bags: Dict[str, Dict[str, int]], multiplier: int, total: int) -> int:
    contents = bags[bag]
    total += sum([multiplier * value for _, value in contents.items()])

    for k, v in contents.items():
        total = bag_counter(k, bags, v * multiplier, total)

    return total


if __name__ == '__main__':
    data = get_input_for_day(2020, 7)
    part_one(data)
    part_two(data)
