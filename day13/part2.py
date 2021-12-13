import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque
import sys


def print_paper(points: set[tuple[int, int]], print=sys.stdout.write):
    max_x, max_y = map(max, zip(*points))

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print('●' if (x, y) in points else ' ')
        print('\n')


with open("input") as inf, open("part2.out", "w+") as outf:
    points = set()

    for line in inf:
        if line.isspace() or len(line) == 0:
            break

        points.add(tuple(map(int, line.strip().split(','))))

    regex = re.compile(r"fold along (x|y)=(\d+)")

    for line in inf:
        m = regex.match(line)
        coord = int(m.group(2))
        axis = m.group(1) == 'x'

        points = {(x, y) for x, y in points if (x if axis else y) < coord} | {
            (2 * coord - x if axis else x, 2 * coord - y if not axis else y)
            for x, y in points
            if (x if axis else y) > coord
        }

    print_paper(points, outf.write)
