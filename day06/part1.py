import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    fishes = list(map(int, inf.readline().split(",")))

    for i in range(80):
        print(i, end="\r")
        new_fishes = Counter(fishes)[0]
        fishes = [6 if f == 0 else f - 1 for f in fishes] + [8] * new_fishes

    outf.write(f"{len(fishes)}\n")
