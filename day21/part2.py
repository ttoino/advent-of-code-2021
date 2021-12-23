import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


@ft.cache
def dirac(p1p, p2p, p1s, p2s, isp1):
    if p1s > 20 or p2s > 20:
        return (int(p1s > 20), int(p2s > 20))

    rp1, rp2 = 0, 0
    for roll in map(sum, it.product(range(1, 4), range(1, 4), range(1, 4))):
        if isp1:
            np1p = (p1p + roll) % 10
            np1s = p1s + np1p + 1
            p1, p2 = dirac(np1p, p2p, np1s, p2s, not isp1)
            rp1 += p1
            rp2 += p2
        else:
            np2p = (p2p + roll) % 10
            np2s = p2s + np2p + 1
            p1, p2 = dirac(p1p, np2p, p1s, np2s, not isp1)
            rp1 += p1
            rp2 += p2

    return rp1, rp2


with open("input") as inf, open("part2.out", "w+") as outf:
    p1p = int(next(inf).split()[-1]) - 1
    p2p = int(next(inf).split()[-1]) - 1

    outf.write(f"{max(dirac(p1p, p2p, 0, 0, True))}\n")
