import typing
import numpy as np
from functools import reduce

from utils.task import print_result


def parse_input(input_file) -> typing.List[int]:
    with open(input_file, 'r') as f:
        return [int(x) for x in f.read().split(',')]

def task_1(positions):
    positions.sort()
    target_pos = positions[round(len(positions)/2)]
    return reduce(lambda a,b: a+b, [abs(pos - target_pos) for pos in positions])

def task_2(positions):
    target_pos = np.floor(np.array(positions).mean())
    return reduce(lambda a,b: a+b, [int((abs(pos - target_pos)*(abs(pos - target_pos)+1))/2) for pos in positions])


if __name__ == '__main__':
    positions = parse_input('day7/input.txt')
    print_result(1,task_1(positions))
    print_result(2,task_2(positions))