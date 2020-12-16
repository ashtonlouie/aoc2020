from collections import Counter, namedtuple, OrderedDict, deque
from typing import Set, Dict, List, Deque
from functools import reduce
from itertools import count
from operator import add
import re
import math

if __name__ == "__main__":

    with open('data/input14.txt') as f:
        data = f.read().splitlines()

    # part 1

    mem = dict()

    block = [data[0]]
    for i in range(1, len(data)):
        if not data[i].startswith('mask'):
            block.append(data[i])
            if i < len(data)-1:
                continue

        # reversed mask
        mask = block[0].split(' ')[-1][::-1]

        for b in block[1:]:
            addr = int(b.split('[')[1].split(']')[0])
            val = int(b.split(' ')[-1])
            for j,m in enumerate(mask):
                if m == 'X':
                    continue
                elif int(m) == 0:
                    val &= ~(1 << j)
                elif int(m) == 1:
                    val |= 1 << j
            mem[addr] = val


        block = [data[i]]

    print(reduce(add, mem.values()))

    # part 2

    mem = dict()

    mask = 0
    for d in data:
        if d.startswith('mask'):
            # reversed mask
            mask = d.split(' ')[-1][::-1]
            continue

        addr = int(d.split('[')[1].split(']')[0])
        val = int(d.split(' ')[-1])
        floating = list()

        for j,m in enumerate(mask):
            if m == 'X':
                floating.append(j)
            elif int(m) == 0:
                continue
            elif int(m) == 1:
                addr |= 1 << j

        addrs = list()

        # we'll get 2^len(floating) addrs
        for k in range(2 ** len(floating)):
            bin_k = format(k, f"0{len(floating)}b")
            base_addr = addr
            for i,b in enumerate(bin_k):
                if int(b) == 0:
                    base_addr &= ~(1 << floating[i])
                elif int(b) == 1:
                    base_addr |= 1 << floating[i]
            addrs.append(base_addr)

        for a in addrs:
            mem[a] = val

    print(reduce(add, mem.values()))


