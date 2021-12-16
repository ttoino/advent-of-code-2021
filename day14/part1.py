import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque

with open("input") as inf, open("part1.out", "w+") as outf:
    polymer = next(inf).strip()
    next(inf)
    rules = dict(line.strip().split(" -> ") for line in inf)

    for i in range(10):
        n = ""

        for first, second in it.pairwise(polymer):
            n += first
            n += rules[first + second]

        n += polymer[-1]
        polymer = n

    c = Counter(polymer).values()

    outf.write(f"{max(c) - min(c)}\n")
