from collections import Counter, namedtuple, OrderedDict, deque
from typing import Set, Dict, List, Deque
from functools import reduce
import re

if __name__ == "__main__":

    with open('data/input10.txt') as f:
        data = f.read().splitlines()
        data = list(map(int, data))

    jolt1 = 0
    jolt3 = 0

    sorted_data = sorted(data)

    # part 1

    prev = 0
    for i in range(len(sorted_data)):
        diff = sorted_data[i] - prev
        if diff == 1:
            jolt1 += 1
        if diff == 3:
            jolt3 += 1
        prev = sorted_data[i]

    jolt3 += 1
    print(jolt1 * jolt3)

    # part 2

    # we know there's only 1 path from the last node
    count = 1
    cache = dict()
    cache[sorted_data[-1]] = 1

    adapters = [0] + sorted_data

    def get_counts(i) -> None:
        curr = adapters[i]
        next_adapters = list()
        j = i + 1
        while j < len(adapters):
            if len(next_adapters) >= 3:
                break
            next = adapters[j]
            if next - curr <= 3:
                next_adapters.append(next)
            else:
                break
            j += 1

        counts = 0
        for n in next_adapters:
            counts += cache[n]

        cache[curr] = counts

    for i in range(len(adapters) - 2, -1, -1):
        get_counts(i)

    print(cache[0])
