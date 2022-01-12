import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque


def operate(t, values):
    match t:
        case 0: return sum(values)
        case 1: return ft.reduce(op.mul, values)
        case 2: return min(values)
        case 3: return max(values)
        case 5: return int(values[0] > values[1])
        case 6: return int(values[0] < values[1])
        case 7: return int(values[0] == values[1])


def parse_packet(packet, start, end = -1) -> tuple[int|None, int|None]:
    if start == end:
        return None, None

    if packet[start:end] == "" or int(packet[start:end], 2) == 0:
        return None, None

    v = int(packet[start:start+3], 2)
    t = int(packet[start+3:start+6], 2)

    if t == 4:
        start += 6
        done = False
        number = ""
        while not done:
            if packet[start] == "0":
                done = True

            number += packet[start+ 1:start+ 5]
            start += 5

        number = int(number, 2)
        return number, start

    values = []
    next_start = None

    i = packet[start+6]

    if i == "1":
        l = int(packet[start+7:start+18], 2)
        index = start + 18
        while l > 0:
            x, index = parse_packet(packet, index)
            l -= 1
            values.append(x)
        next_start = index

    else:
        l = int(packet[start+7:start+22], 2)
        end = start + 22 + l
        index = start + 22
        prev_index = None
        while index != None:
            prev_index = index
            x, index = parse_packet(packet, index, end)
            values.append(x)
        values = values[:-1]  # Remove last None
        next_start = prev_index

    return operate(t, values), next_start


with open("input") as inf, open("part2.out", "w+") as outf:
    packet = "".join(f"{int(x, 16):04b}" for x in next(inf).strip())

    outf.write(f"{parse_packet(packet, 0)[0]}\n")
