import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque

with open("input") as inf, open("part1.out", "w+") as outf:
    octopi = list(map(lambda x: list(map(int, x.strip())), inf))

    w = len(octopi[0])
    h = len(octopi)

    result = 0

    for i in range(100):
        flashed: set[tuple[int, int]] = set()

        # step 1
        octopi = [[o + 1 for o in l] for l in octopi]

        # step 2
        f = True
        while f:
            f = False

            for x, y in it.product(range(w), range(h)):
                if octopi[y][x] > 9 and (x, y) not in flashed:
                    flashed.add((x, y))
                    f = True
                    for dx, dy in it.product(range(-1, 2), range(-1, 2)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < w and 0 <= ny < h:
                            octopi[ny][nx] += 1

        # step 3
        octopi = [[0 if o > 9 else o for o in l] for l in octopi]
        result += len(flashed)

    outf.write(f"{result}\n")
