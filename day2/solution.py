import typing
from collections import namedtuple

from utils.task import print_result

Movement = namedtuple('Movement', ['direction', 'distance'])

def parse_movement(movement:str) -> Movement:
    tokens = movement.split(' ')
    direction = tokens[0]
    distance = int(tokens[1])
    return Movement(direction, distance)

def parse_input(filename:str) -> typing.List[Movement]:
    with open(filename, 'r') as f:
        return [parse_movement(line) for line in f.readlines()]

def task_1(movements:typing.List[Movement]) -> int:
    depth = 0
    horizontal = 0
    for movement in movements:
        if movement.direction == 'down':
            depth += movement.distance
        elif movement.direction == 'up':
            depth -= movement.distance
        elif movement.direction == 'forward':
            horizontal += movement.distance

    return horizontal * depth


def task_2(movements:typing.List[Movement]) -> int:
    depth = 0
    horizontal = 0
    aim = 0

    for movement in movements:
        if movement.direction == 'down':
            aim += movement.distance
        elif movement.direction == 'up':
            aim -= movement.distance
        elif movement.direction == 'forward':
            horizontal += movement.distance
            depth += aim * movement.distance

    return horizontal * depth

if __name__ == "__main__":
    movements = parse_input('/Users/aleksandar/projects/advent-of-code/2021/day2/input.txt');
    print_result(1,task_1(movements))
    print_result(1,task_2(movements))
