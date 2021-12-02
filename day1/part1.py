import itertools as it

with open("input") as inf, open("part1", "w+") as outf:
    increases = sum(curr > prev for prev, curr in it.pairwise(map(int, inf)))

    outf.write(f"{increases}\n")
