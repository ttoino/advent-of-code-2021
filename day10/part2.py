import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque

closing_brackets = (')', ']', '}', '>')
opening_brackets = {'(': 1, '[': 2, '{': 3, '<': 4}
bracket_map = {')': '(', ']': '[', '}': '{', '>': '<'}


def error_score(line: str):
    brackets = deque()
    for bracket in line:
        if bracket in opening_brackets:
            brackets.append(bracket)
        if bracket in closing_brackets:
            if brackets.pop() != bracket_map[bracket]:
                return 0

    score = 0
    while len(brackets):
        score *= 5
        score += opening_brackets[brackets.pop()]

    return score


with open("input") as inf, open("part2.out", "w+") as outf:
    scores = map(error_score, inf)

    scores = sorted(s for s in scores if s)

    outf.write(f"{scores[len(scores)//2]}\n")
