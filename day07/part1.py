import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    crabs = list(map(int, inf.readline().split(",")))

    pos = sorted(crabs)[len(crabs) // 2]

    outf.write(f"{sum(abs(pos - x) for x in crabs)}\n")
