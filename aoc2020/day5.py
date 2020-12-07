from collections import Counter, namedtuple, OrderedDict
from typing import Set
import re

if __name__ == "__main__":

    with open('data/input5.txt') as f:
        data = f.read().splitlines()


    def binary_search(input, l, h):
        curr = input[0]
        if len(input) == 1:
            return l if (curr == 'F' or curr == 'L') else h
        next_input = input[1:]

        if curr == 'F' or curr == 'L':
            next_h = ((h + l) // 2)
            next_l = l
        else:
            next_h = h
            next_l = ((h + l) // 2) + 1

        return binary_search(next_input, next_l, next_h)


    ids = set()
    max_id = 0

    potential_my_ids = set()
    def check_my_id(ids, id, potential_my_ids):
        if (id + 2) in ids and (id + 1) not in potential_my_ids:
            potential_my_ids.add(id + 1)
        elif (id - 2) in ids and (id - 1) not in potential_my_ids:
            potential_my_ids.add(id - 1)


    for d in data:
        row = d[:7]
        col = d[7:]

        r = binary_search(row, 0, 127)
        c = binary_search(col, 0, 7)

        id = r * 8 + c
        ids.add(id)

        check_my_id(ids, id, potential_my_ids)

        if id > max_id:
            max_id = id

    # part 1 answer
    print(max_id)

    # part 2 answer
    for id in potential_my_ids:
        if (id + 1) in ids and (id - 1) in ids and id not in ids:
            print(id)
