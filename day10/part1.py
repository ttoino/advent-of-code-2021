import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque

closing_brackets = {')': 3, ']': 57, '}': 1197, '>': 25137}
opening_brackets = ('(', '[', '{', '<')
bracket_map = {')': '(', ']': '[', '}': '{', '>': '<'}


def error_score(line: str):
    brackets = deque()
    for bracket in line:
        if bracket in opening_brackets:
            brackets.append(bracket)
        if bracket in closing_brackets:
            if brackets.pop() != bracket_map[bracket]:
                return closing_brackets[bracket]

    return 0


with open("input") as inf, open("part1.out", "w+") as outf:
    scores = map(error_score, inf)

    outf.write(f"{sum(x*y for x, y in Counter(scores).items())}\n")
