import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque

with open("input") as inf, open("part2.out", "w+") as outf:
    polymer = next(inf).strip()
    last = polymer[-1]
    polymer = Counter(it.pairwise(polymer))
    next(inf)
    rules = dict(line.strip().split(" -> ") for line in inf)

    for i in range(40):
        temp = Counter()

        for (first, second), frequency in polymer.items():
            middle = rules[first + second]

            temp[first, middle] += frequency
            temp[middle, second] += frequency

        polymer = temp

    c = Counter(last)
    for (first, second), frequency in polymer.items():
        c[first] += frequency

    outf.write(f"{max(c.values()) - min(c.values())}\n")
