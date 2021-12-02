import itertools as it

with open("input") as inf, open("part2.out", "w+") as outf:
    increases = sum(curr > prev for prev, curr in it.pairwise(map(sum, ((a, b, c) for (a, _), (b, c) in it.pairwise(it.pairwise(map(int, inf)))))))

    outf.write(f"{increases}\n")
