import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

visited_pos = set()


def visit(x, y):
    if x >= w or x < 0 or y >= h or y < 0 or (x, y) in visited_pos:
        return 0

    v = height_map[y][x]
    visited_pos.add((x, y))

    if v == 9:
        return 0

    return 1 + visit(x + 1, y) + visit(x - 1, y) + visit(x, y + 1) + visit(
        x, y - 1)


with open("input") as inf, open("part2.out", "w+") as outf:
    global height_map, w, h
    height_map = tuple(map(lambda x: tuple(map(int, x.strip())), inf))
    w, h = len(height_map[0]), len(height_map)

    areas = sorted(visit(x, y) for x, y in it.product(range(w), range(h)))

    outf.write(f"{ft.reduce(op.mul, areas[-3:], 1)}\n")
