import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    fishes = list(map(int, inf.readline().split(",")))

    zeros = Counter(fishes)
    new_zeros = Counter()

    for i in range(256):
        new_zeros[(i + 2) % 7] = zeros[i % 7]
        zeros[i % 7] += new_zeros[i % 7]
        new_zeros[i % 7] = 0

    outf.write(f"{sum(zeros.values()) + sum(new_zeros.values())}\n")
