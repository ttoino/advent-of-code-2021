import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    regex = re.compile(r",|(?: -> )")

    lines = filter(lambda x: x[0] == x[2] or x[1] == x[3],
                   map(lambda x: tuple(map(int, x)), map(regex.split, inf)))

    l = []
    for line in lines:
        x1, y1, x2, y2 = line
        for p in it.product(range(min(x1, x2),
                                  max(x1, x2) + 1),
                            range(min(y1, y2),
                                  max(y1, y2) + 1)):
            l.append(p)

    outf.write(f"{len([c for _, c in Counter(l).items() if c >= 2])}\n")
