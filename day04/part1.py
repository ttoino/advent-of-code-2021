import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
from collections import Counter
from typing import Iterable


def verify_solved(boards: list[tuple[tuple[int, ...], ...]]):
    for b in boards:
        for r in it.chain(b, zip(*b)):
            if sum(r) == 5 * 255:
                return b

    return False


with open("input") as inf, open("part1.out", "w+") as outf:
    numbers = map(int, inf.readline().split(","))

    boards = [
        tuple(
            tuple(int(i)
                  for i in line.split())
            for line in b
            if line != "\n")
        for b in mit.grouper(inf, 6)
    ]

    b = False
    n = 0
    while not (b := verify_solved(boards)):
        n = next(numbers)

        boards = [
            tuple(tuple(255 if i == n else i
                        for i in r)
                  for r in b)
            for b in boards
        ]

    outf.write(f"{n * sum(filter(lambda x: x != 255, sum(b, ())))}\n")
