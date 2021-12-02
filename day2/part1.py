import itertools as it
import functools as ft

opmap = {
    "forward": lambda p, x: (p[0] + x, p[1]),
    "up": lambda p, x: (p[0], p[1] - x),
    "down": lambda p, x: (p[0], p[1] + x)
}

with open("input") as inf, open("part1.out", "w+") as outf:
    x, y = ft.reduce(lambda p, x: opmap[x[0]](p, int(x[1])),
                     map(lambda x: x.split(), inf), (0, 0))

    outf.write(f"{x * y}\n")
