import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    regex = re.compile(r",|(?: -> )")

    lines = map(lambda x: tuple(map(int, x)), map(regex.split, inf))

    l = []
    for line in lines:
        x1, y1, x2, y2 = line
        xstep = 1 if x1 < x2 else -1
        ystep = 1 if y1 < y2 else -1
        for p in it.zip_longest(range(x1, x2 + xstep, xstep),
                                range(y1, y2 + ystep, ystep),
                                fillvalue=x1 if x1 == x2 else y1):
            l.append(p)

    outf.write(f"{len([c for _, c in Counter(l).items() if c >= 2])}\n")
