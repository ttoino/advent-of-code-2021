import itertools as it
import functools as ft

opmap = {
    "forward": lambda p, x: (p[0] + x, p[1] + p[2] * x, p[2]),
    "up": lambda p, x: (p[0], p[1], p[2] - x),
    "down": lambda p, x: (p[0], p[1], p[2] + x)
}

with open("input") as inf, open("part2.out", "w+") as outf:
    x, y, _ = ft.reduce(lambda p, x: opmap[x[0]](p, int(x[1])),
                        map(lambda x: x.split(), inf), (0, 0, 0))

    outf.write(f"{x * y}\n")
