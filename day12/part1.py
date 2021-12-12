import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque


def get_paths(path: list[str], graph: dict[str, set[str]]):
    current = path[-1]

    if current == "end":
        return 1

    # remove current if small
    if current.islower():
        graph = {k: v - {current} for k, v in graph.items()}

    return sum(get_paths(path + [n], graph) for n in graph[current])


with open("input") as inf, open("part1.out", "w+") as outf:
    graph = dict()

    for l in inf:
        n1, n2 = l.strip().split('-')

        if n1 not in graph:
            graph[n1] = set()
        if n2 not in graph:
            graph[n2] = set()

        graph[n1].add(n2)
        graph[n2].add(n1)

    outf.write(f"{get_paths(['start'], graph)}\n")
