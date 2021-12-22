import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    regex = re.compile(
        r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)"
    )

    lines = (regex.match(s).group(2, 3, 4, 5, 6, 7, 1) for s in inf if s)

    cubes = set()
    for line in lines:
        min_x, max_x, min_y, max_y, min_z, max_z = int(line[0]), int(
            line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5])

        if min_x > 50 or min_y > 50 or min_z > 50 or max_x < -50 or max_y < -50 or max_z < -50:
            continue

        new_cubes = set(
            it.product(range(min_x, max_x + 1), range(min_y, max_y + 1),
                       range(min_z, max_z + 1)))

        if line[6] == "on":
            cubes |= new_cubes
        else:
            cubes -= new_cubes

    outf.write(f"{len(cubes)}\n")
