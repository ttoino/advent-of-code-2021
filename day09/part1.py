import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def is_localmin(hm: tuple[tuple[int, ...], ...], pos, size):
    x, y = pos
    w, h = size

    for dx, dy in it.product(range(-1, 2), range(-1, 2)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h and hm[ny][nx] < hm[y][x]:
            return False

    return True


with open("input") as inf, open("part1.out", "w+") as outf:
    height_map = tuple(map(lambda x: tuple(map(int, x.strip())), inf))
    size = len(height_map[0]), len(height_map)

    r = sum(v + 1
            for y, line in enumerate(height_map)
            for x, v in enumerate(line)
            if is_localmin(height_map, (x, y), size))

    outf.write(f"{r}\n")
