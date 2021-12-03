import functools
import typing
from copy import deepcopy

from utils.task import print_result

def parse_input(filename:str) -> typing.List[str]:
    with open(filename) as f:
        return f.read().splitlines()

def sum_bin(x, y):
    return [int(x) + int(y) for (x,y) in zip(x,y)]

def get_gama_eps(measurments):
    gamma = list(map(lambda x: '1' if int(x) >= (len(measurments)/2) else '0',functools.reduce(lambda x, y: sum_bin(x,y), measurments)))
    eps = list(map(lambda x: '1' if x == '0' else '0', gamma))
    return gamma, eps

def task_1(measurments):
    gamma, eps = get_gama_eps(measurments)

    return int(''.join(gamma),2) * int(''.join(eps),2)

def task_2(measurments):
    o, c = 0, 0
    oxygen_ratings = deepcopy(measurments)
    co2_ratings = deepcopy(measurments)


    for i in range(len(measurments[0])):
        if len(oxygen_ratings)==1:
            break
        gamma, _ = get_gama_eps(oxygen_ratings)
        oxygen_ratings = list(filter(lambda x: x[i] == gamma[i], oxygen_ratings))
    
    for i in range(len(measurments[0])):
        if len(co2_ratings)==1:
            break
        _, eps = get_gama_eps(co2_ratings)
        co2_ratings = list(filter(lambda x: x[i] == eps[i], co2_ratings))

    return int(''.join(oxygen_ratings[0]),2) * int(''.join(co2_ratings[0]),2)


if __name__ == "__main__":
    measurments = parse_input("/Users/aleksandar/projects/advent-of-code/2021/day3/input.txt")
    print_result(1,task_1(measurments))
    print_result(2,task_2(measurments))
