import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
from collections import Counter
from typing import Iterable


def verify_solved(board: tuple[tuple[int, ...], ...]):
    for r in it.chain(board, zip(*board)):
        if sum(r) == 5 * 255:
            return True

    return False


with open("input") as inf, open("part2.out", "w+") as outf:
    numbers = map(int, inf.readline().split(","))

    boards = [
        tuple(
            tuple(int(i)
                  for i in line.split())
            for line in b
            if line != "\n")
        for b in mit.grouper(inf, 6)
    ]

    b = ()
    n = 0
    while len(boards) > 0:
        n = next(numbers)

        boards = [
            tuple(tuple(255 if i == n else i
                        for i in r)
                  for r in b)
            for b in boards
        ]

        b = boards[0]
        boards = [b for b in boards if not verify_solved(b)]

    outf.write(f"{n * sum(filter(lambda x: x != 255, sum(b, ())))}\n")
