import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    # inf = [
    #     "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    #     "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    #     "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    #     "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    #     "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    #     "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    #     "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    #     "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    #     "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    #     "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
    # ]
    lines = map(lambda x: map(lambda x: x.split(), x.split("|")), inf)

    o = 0
    for samples, outputs in lines:
        # Sort by length so it's easier to separate them
        samples = sorted(samples, key=len)

        # Get known representations
        digits = {1: samples[0], 7: samples[1], 4: samples[2], 8: samples[-1]}
        # Separate unknown representations
        len5 = samples[3:6]
        len6 = samples[6:-1]

        # Get b and d segments
        middle_bit = set(digits[4]) - set(digits[1])

        # Find 3
        for i in len5:
            if set(i).issuperset(set(digits[1])):
                digits[3] = i
                len5.remove(i)
                break

        # Find 9
        for i in len6:
            if set(i).issuperset(set(digits[3])):
                digits[9] = i
                len6.remove(i)
                break

        # Find 0
        for i in len6:
            if set(i).issuperset(set(digits[1])):
                digits[0] = i
                len6.remove(i)
                break
        # 6 is left
        digits[6] = len6[0]

        # Find 5
        for i in len5:
            if set(i).issubset(set(digits[6])):
                digits[5] = i
                len5.remove(i)
                break
        # 2 is left
        digits[2] = len5[0]

        # There's definitely a better way to do this
        digits = dict((frozenset(y), str(x)) for x, y in digits.items())
        o += int("".join(digits[frozenset(d)] for d in outputs))

    outf.write(f"{o}\n")
