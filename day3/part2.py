import itertools as it
import functools as ft
import operator as op
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    ll = list(inf)
    l = list(ll)
    i = 0

    while len(l) > 1:
        c = Counter(n[i] for n in l).most_common(2)
        mcb = '1' if c[0][1] == c[-1][1] else c[0][0]
        l = list(filter(lambda x: x[i] == mcb, l))
        i += 1

    ogr = int(l[0], 2)

    l = list(ll)
    i = 0

    while len(l) > 1:
        c = Counter(n[i] for n in l).most_common(2)
        lcb = '0' if c[0][1] == c[-1][1] else c[-1][0]
        l = list(filter(lambda x: x[i] == lcb, l))
        i += 1

    co2sr = int(l[0], 2)

    outf.write(f"{ogr * co2sr}\n")
