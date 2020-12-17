from collections import Counter, namedtuple, OrderedDict, deque
from typing import Set, Dict, List, Deque
from functools import reduce
from itertools import count, chain
from operator import add
import re
import math

if __name__ == "__main__":

    with open('data/input16.txt') as f:
        data = f.read().splitlines()

    fields = list()

    temp = list()
    for i,d in enumerate(data):
        if not d:
            fields.append(temp)
            temp = list()
            continue
        temp.append(d)
        if i == len(data) - 1:
            fields.append(temp)

    rule_ranges = [list(map(int, chain(*map(lambda x: x.split('-'), r.split(': ')[1].split(' or '))))) for r in fields[0]]
    mine = [int(m) for m in fields[1][1].split(',')]
    tickets = [list(map(int, t.split(','))) for t in fields[2][1:]]
    real_tickets = list()

    # part 1

    valid = set()
    for r in rule_ranges:
        for x in range(r[0], r[1]+1):
            valid.add(x)
        for x in range(r[2], r[3]+1):
            valid.add(x)

    invalid = list()
    for i,t in enumerate(tickets):
        discard = False
        for val in t:
            if val not in valid:
                discard = True
                invalid.append(val)
        if not discard:
            real_tickets.append(t)

    print(reduce(add,invalid))

    # part 2

    rule_names = [x.split(':')[0] for x in fields[0]]
    rules = dict(zip(rule_names, rule_ranges))

    possibilities = dict()
    for i in range(len(real_tickets[0])):
        candidates = rules.copy()
        for j in range(len(real_tickets)):
            val = real_tickets[j][i]
            to_delete = list()
            for name,ranges in candidates.items():
                pair1 = set(range(ranges[0], ranges[1]+1))
                pair2 = set(range(ranges[2], ranges[3]+1))
                if not (val in pair1 or val in pair2):
                    to_delete.append(name)
            for name in to_delete:
                del candidates[name]
        possibilities[i] = set(candidates.keys())

    positions = dict()
    while len(positions) < len(rules):
        for i,names in possibilities.items():
            if len(names) == 1:
                n = names.pop()
                positions[n] = i
                for j in range(len(possibilities)):
                    possibilities[j].discard(n)

    product = 1
    for name,i in positions.items():
        if name.startswith('departure'):
            product *= mine[i]

    print(product)
