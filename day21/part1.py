import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    p1_pos = int(next(inf).split()[-1]) - 1
    p2_pos = int(next(inf).split()[-1]) - 1

    p1_score = 0
    p2_score = 0

    die = it.cycle(range(1, 101))
    die_count = 0

    is_p1_turn = True

    while p1_score < 1000 and p2_score < 1000:
        if is_p1_turn:
            p1_pos = (p1_pos + next(die) + next(die) + next(die)) % 10
            p1_score += p1_pos + 1
        else:
            p2_pos = (p2_pos + next(die) + next(die) + next(die)) % 10
            p2_score += p2_pos + 1

        die_count += 3
        is_p1_turn = not is_p1_turn

    outf.write(
        f"{die_count * (p2_score if p2_score < p1_score else p1_score)}\n")
