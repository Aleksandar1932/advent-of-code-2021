import typing
import os

INPUT_FILE = os.getenv("INPUT_FILE") or "./input.txt"

def parse_input(filename:str) -> typing.List[int]:
    with open(filename) as f:
        return [int(line) for line in f]

def task_1(measurements:list) -> typing.Tuple[int,int]:
    increases, decreases = 0, 0

    for i in range(len(measurements)):
        if i == 0:
            continue
        if measurements[i] > measurements[i - 1]:
            increases += 1
        elif measurements[i] < measurements[i - 1]:
            decreases += 1
    
    return increases, decreases


def task_2(measurements,window_size = 3) -> typing.Tuple[int,int]:
    window_sums = []

    for i in range((len(measurements)-window_size+1)):
        window_sums.append(sum(measurements[i:i + window_size]))

    return task_1(window_sums)

def print_result(task:int, result) -> typing.Callable:
    print(f"Task {task}:{result}")

if __name__ == "__main__":
    measurements = parse_input(INPUT_FILE)
    print_result(1,task_1(measurements))
    print_result(2,task_2(measurements))