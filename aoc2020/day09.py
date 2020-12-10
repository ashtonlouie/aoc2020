from collections import Counter, namedtuple, OrderedDict, deque
from typing import Set, Dict, List, Deque
from functools import reduce
import re

if __name__ == "__main__":

    with open('data/input09.txt') as f:
        data = f.read().splitlines()
        data = list(map(int, data))

    window = deque()

    # preamble
    for i in range(25):
        window.append(data[i])


    # part 1

    def check_valid(window: Deque, target: int) -> bool:
        for j in range(len(window)):
            diff = target - window[j]
            if diff < 0:
                continue
            for k in range(len(window)):
                if j == k:
                    continue
                if diff == window[k]:
                    return True
        return False


    first_invalid = 0
    for i in range(25, len(data)):
        if not check_valid(window, data[i]):
            first_invalid = data[i]
            break

        window.append(data[i])
        window.popleft()

    print(first_invalid)

    # part 2

    contig = deque()
    output_sum = 0

    from operator import add

    for i in range(len(data)):
        if len(contig) < 2:
            contig.append(data[i])
            continue

        sum = reduce(add, contig)

        while sum > first_invalid:
            sum -= contig.popleft()

        if sum == first_invalid:
            sorted_contig = sorted(contig)
            output_sum = sorted_contig[0] + sorted_contig[-1]
            break

        contig.append(data[i])

    print(output_sum)
