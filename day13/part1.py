import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque

with open("input") as inf, open("part1.out", "w+") as outf:
    points = set()

    for line in inf:
        if line.isspace() or len(line) == 0:
            break

        points.add(tuple(map(int, line.strip().split(','))))

    regex = re.compile(r"fold along (x|y)=(\d+)")

    m = regex.match(next(inf))
    coord = int(m.group(2))
    axis = m.group(1) == 'x'

    points = {(x, y) for x, y in points if (x if axis else y) < coord} | {
        (2 * coord - x if axis else x, 2 * coord - y if not axis else y)
        for x, y in points
        if (x if axis else y) > coord
    }

    outf.write(f"{len(points)}\n")
