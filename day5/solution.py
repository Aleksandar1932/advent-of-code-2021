from collections import namedtuple
from collections import Counter
import typing

from utils.task import print_result

Point = namedtuple('Point', ['x', 'y'])


def parse_input(input_file) -> typing.List[typing.List[Point]]:
    lines = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            p1, p2 = line.split('-> ')
            lines.append([Point(*[int(x) for x in p1.split(',')]),
                         Point(*[int(x) for x in p2.split(',')])])

    return lines


def make_line(p1, p2):
    x, y = [], []
    for axis in ['x', 'y']:
        reverse = False
        start = getattr(p1, axis)
        end = getattr(p2, axis)

        if (start > end):
            reverse = True

        if axis == 'x':
            if not reverse:
                x = list(range(start, end+1))
            else:
                x = list(range(end, start+1))
                x.reverse()

        else:
            if not reverse:
                y = list(range(start, end+1))
            else:
                y = list(range(end, start+1))
                y.reverse()

    if len(x) == 1:
        x = [p1.x]*len(y)

    if len(y) == 1:
        y = [p1.y]*len(x)

    return list(zip(x, y))


def task_1(lines):
    points = []
    for line in lines:
        if line[0].x == line[1].x or line[0].y == line[1].y:
            points.extend(make_line(line[0], line[1]))

    counts = Counter(points).values()
    return len([x for x in counts if x > 1])


def task_2(lines):
    points = []
    for line in lines:
        points.extend(make_line(line[0], line[1]))

    counts = Counter(points).values()
    return len([x for x in counts if x > 1])


if __name__ == "__main__":
    lines = parse_input('day5/input.txt')
    print_result(1, task_1(lines))
    print_result(2, task_2(lines))
