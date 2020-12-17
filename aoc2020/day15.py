from collections import Counter, namedtuple, OrderedDict, deque
from typing import Set, Dict, List, Deque
from functools import reduce
from itertools import count
from operator import add
import re
import math

if __name__ == "__main__":

    with open('data/input15.txt') as f:
        data = f.read().splitlines()

    nums = list(map(int, data[0].split(',')))

    seen = dict()
    turn = 1
    last = 0

    for n in nums:
        # deque will always have 2 elements: [lastlast time seen, last time seen]
        d = deque()
        d.append(turn)
        seen[n] = d
        last = n
        turn += 1

    while True:
        if len(seen[last]) == 1:
            curr = 0
        else:
            curr = seen[last][1] - seen[last][0]

        if curr not in seen:
            d = deque()
            d.append(turn)
            seen[curr] = d
        else:
            if len(seen[curr]) > 1:
                seen[curr].popleft()
            seen[curr].append(turn)

        last = curr
        if turn == 30000000:
            break
        turn += 1

    # part 2 has terrible performance this way but it works :)

    print(last)