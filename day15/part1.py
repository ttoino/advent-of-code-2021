import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque
import heapq

offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]

with open("input") as inf, open("part1.out", "w+") as outf:
    grid = [[int(x) for x in l.strip()] for l in inf]

    width = len(grid)
    height = len(grid[0])

    heap = [(0, 0, 0)]
    heapq.heapify(heap)
    visited = set()

    while len(heap):
        c, x, y = heapq.heappop(heap)

        if x == width - 1 and y == height - 1:
            outf.write(f"{c}\n")
            break

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in offsets:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                heapq.heappush(heap, (c + grid[nx][ny], nx, ny))

    # outf.write(f"{0}\n")
