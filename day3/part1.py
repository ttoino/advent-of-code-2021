import itertools as it
import functools as ft
import operator as op
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    gamma, epsilon = map(lambda x: int(x, 2), ft.reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), map(lambda c: (c.most_common(1)[0][0], c.most_common(2)[-1][0]), map(Counter, zip(*inf)))))

    outf.write(f"{gamma * epsilon}\n")
