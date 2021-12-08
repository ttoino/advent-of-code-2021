import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    easy_lens = (2, 3, 4, 7)
    lines = map(lambda x: x.split("|")[1].split(), inf)

    outf.write(
        f"{ft.reduce(lambda x, y: x + (len(y) in easy_lens), ft.reduce(op.add, lines), 0)}\n"
    )
