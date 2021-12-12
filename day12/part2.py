import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque


def get_paths(path: list[str], graph: dict[str, set[str]], visited_twice: bool):
    current = path[-1]

    if current == "end":
        return 1

    if len(graph["end"]) == 0:
        return 0

    # remove current if small
    if current.islower():
        if current.endswith(' '):
            visited_twice = True
            graph = {
                k: {x for x in v if not x.endswith(' ')
                   } for k, v in graph.items()
            }
        elif visited_twice or current == "start":
            graph = {k: v - {current} for k, v in graph.items()}
        else:
            graph = {
                k: {x + ' ' if x == current else x for x in v
                   } for k, v in graph.items()
            }

    return sum(
        get_paths(path + [n], graph, visited_twice)
        for n in graph[current.strip()])


with open("input") as inf, open("part2.out", "w+") as outf:
    graph = dict()

    for l in inf:
        n1, n2 = l.strip().split('-')

        if n1 not in graph:
            graph[n1] = set()
        if n2 not in graph:
            graph[n2] = set()

        graph[n1].add(n2)
        graph[n2].add(n1)

    outf.write(f"{get_paths(['start'], graph, False)}\n")
