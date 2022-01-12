import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque


def parse_packet(packet, count=-1):
    if packet == "" or int(packet, 2) == 0:
        return 0

    if count == 0:
        return parse_packet(packet, count - 1)

    v = int(packet[:3], 2)
    t = int(packet[3:6], 2)

    if t == 4:
        i = 6
        done = False
        number = ""
        while not done:
            if packet[i] == "0":
                done = True

            number += packet[i + 1:i + 5]
            i += 5

        number = int(number, 2)
        return v + parse_packet(packet[i:], count - 1)

    i = packet[6]

    if i == "1":
        l = int(packet[7:18], 2)
        return v + parse_packet(packet[18:], l)

    else:
        l = int(packet[7:22], 2)
        return v + parse_packet(packet[22:22 + l], -1) + parse_packet(
            packet[22 + l:], count - 1)


with open("input") as inf, open("part1.out", "w+") as outf:
    packet = "".join(f"{int(x, 16):04b}" for x in next(inf).strip())

    outf.write(f"{parse_packet(packet)}\n")
