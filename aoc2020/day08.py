from collections import Counter, namedtuple, OrderedDict
from typing import Set, Dict, List
from functools import reduce
import re

if __name__ == "__main__":


    with open('data/input08.txt') as f:
        data = f.read().splitlines()

    # part 1

    acc = 0
    i = 0
    visited = set()
    while i < len(data):
        if i in visited:
            break
        visited.add(i)

        op = data[i].split(' ')[0]
        arg = int(data[i].split(' ')[1])
        if op == 'nop':
            i += 1
        elif op == 'acc':
            acc += arg
            i += 1
        elif op == 'jmp':
            i += arg

    print(acc)

    # part 2

    acc = 0
    i = 0
    visited = set()
    Op = namedtuple('Op', ['index', 'op', 'arg', 'acc_snapshot'])
    prev = None
    visited_since = list()
    changed = False
    skip_next_change = False

    while i < len(data):
        if i in visited:
            visited.remove(prev.index)
            i = prev.index
            acc = prev.acc_snapshot

            while visited_since:
                visited.remove(visited_since.pop())
            prev = None
            changed = False
            skip_next_change = True
            continue

        if prev:
            visited_since.append(i)

        visited.add(i)

        op = data[i].split(' ')[0]
        arg = int(data[i].split(' ')[1])

        if op == 'nop':
            if not changed and not skip_next_change:
                prev = Op(i, op, arg, acc)
                changed = True
                i += arg
                continue
            i += 1
            if skip_next_change:
                skip_next_change = False
        elif op == 'acc':
            acc += arg
            i += 1
        elif op == 'jmp':
            if not changed and not skip_next_change:
                prev = Op(i, op, arg, acc)
                changed = True
                i += 1
                continue
            i += arg
            if skip_next_change:
                skip_next_change = False


    print(acc)
