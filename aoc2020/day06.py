from collections import Counter, namedtuple, OrderedDict
from typing import Set
from functools import reduce
import re

if __name__ == "__main__":

    with open('data/input06.txt') as f:
        data = f.read().splitlines()

    # part 1
    total = 0

    group = set()
    for i in range(len(data)):
        if not data[i]:
            total += len(group)
            group = set()
            continue

        for c in data[i]:
            group.add(c)

        if i == len(data) - 1:
           total += len(group)


    print(total)

    # part 2

    total = 0

    group = list()
    for i in range(len(data)):
        if not data[i]:
            total += len(reduce(lambda s1,s2: s1.intersection(s2), group))
            group = list()
            continue

        group.append(set(data[i]))

        if i == len(data) - 1:
            total += len(reduce(lambda s1, s2: s1.intersection(s2), group))


    print(total)