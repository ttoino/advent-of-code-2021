import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def t(x):
    return x * (x + 1) // 2


with open("input") as inf, open("part2.out", "w+") as outf:
    crabs = list(map(int, inf.readline().split(",")))

    f = min(sum(t(abs(i - x)) for x in crabs) for i in range(max(crabs)))

    outf.write(f"{f}\n")
