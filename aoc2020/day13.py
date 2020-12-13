from collections import Counter, namedtuple, OrderedDict, deque
from typing import Set, Dict, List, Deque
from functools import reduce
from itertools import count
import re
import math

if __name__ == "__main__":

    with open('data/input13.txt') as f:
        data = f.read().splitlines()

    time = int(data[0])
    buses = list()
    for d in data[1].split(','):
        if d == 'x':
            continue
        buses.append(int(d))

    # part 1

    timediff = float('inf')
    shortest_bus = 0
    for b in buses:
        next_depart = b * math.ceil(time / b)
        diff = next_depart - time
        if diff < timediff:
            timediff = diff
            shortest_bus = b

    print(timediff * shortest_bus)

    # part 2

    Bus = namedtuple('Bus', ['time', 'idx'])
    buses = list()
    dsplit = data[1].split(',')
    for i in range(len(dsplit)):
        if dsplit[i] == 'x':
            continue
        buses.append(Bus(int(dsplit[i]), i))

    sorted_buses = sorted(buses, key=lambda b: b.time, reverse=True)

    i = 0
    steps = 1
    for time, idx in sorted_buses:
        for base_time in count(i, steps):
            if (base_time + idx) % time == 0:
                i = base_time
                steps *= time
                break
    print(base_time)


