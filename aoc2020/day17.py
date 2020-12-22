from collections import Counter, namedtuple, OrderedDict, deque, defaultdict
from typing import Set, Dict, List, Deque
from functools import reduce
from itertools import count, chain
from operator import add
import re
import math

if __name__ == "__main__":
    with open('data/input17.txt') as f:
        data = f.read().splitlines()

    Cube = namedtuple('Cube', ['x', 'y', 'z'])

    # node[z][y][x]: node dict (z) holds dicts y which hold set x.
    # this gives tree lookup time and practically infinite bidirectional indexing
    node = dict()  # z
    node[0] = dict()  # y
    node[0][0] = set()  # x

    active_nodes = set()

    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '#':
                active_nodes.add(Cube(x, y, 0))
                if y not in node[0]:
                    node[0][y] = set()
                node[0][y].add(x)

    def get_neighbors(c: Cube) -> Set:
        neighbors = set()
        neighbors.add(Cube(c.x, c.y, c.z + 1))
        neighbors.add(Cube(c.x, c.y, c.z - 1))
        neighbors.add(Cube(c.x, c.y + 1, c.z))
        neighbors.add(Cube(c.x, c.y + 1, c.z + 1))
        neighbors.add(Cube(c.x, c.y + 1, c.z - 1))
        neighbors.add(Cube(c.x, c.y - 1, c.z))
        neighbors.add(Cube(c.x, c.y - 1, c.z + 1))
        neighbors.add(Cube(c.x, c.y - 1, c.z - 1))
        neighbors.add(Cube(c.x + 1, c.y, c.z))
        neighbors.add(Cube(c.x + 1, c.y, c.z + 1))
        neighbors.add(Cube(c.x + 1, c.y, c.z - 1))
        neighbors.add(Cube(c.x + 1, c.y + 1, c.z))
        neighbors.add(Cube(c.x + 1, c.y + 1, c.z + 1))
        neighbors.add(Cube(c.x + 1, c.y + 1, c.z - 1))
        neighbors.add(Cube(c.x + 1, c.y - 1, c.z))
        neighbors.add(Cube(c.x + 1, c.y - 1, c.z + 1))
        neighbors.add(Cube(c.x + 1, c.y - 1, c.z - 1))
        neighbors.add(Cube(c.x - 1, c.y, c.z))
        neighbors.add(Cube(c.x - 1, c.y, c.z + 1))
        neighbors.add(Cube(c.x - 1, c.y, c.z - 1))
        neighbors.add(Cube(c.x - 1, c.y + 1, c.z))
        neighbors.add(Cube(c.x - 1, c.y + 1, c.z + 1))
        neighbors.add(Cube(c.x - 1, c.y + 1, c.z - 1))
        neighbors.add(Cube(c.x - 1, c.y - 1, c.z))
        neighbors.add(Cube(c.x - 1, c.y - 1, c.z + 1))
        neighbors.add(Cube(c.x - 1, c.y - 1, c.z - 1))
        return neighbors

    def process_neighbors(c: Cube, active: bool, already_checked: Set):
        neighbors = get_neighbors(c)
        active_neighbors = set()
        inactive_neighbors = set()
        for n in neighbors:
            if n in already_checked:
                continue
            if n.z not in node:
                node[n.z] = dict()
            if n.y not in node[n.z]:
                node[n.z][n.y] = set()
            if n.x not in node[n.z][n.y]:
                inactive_neighbors.add(n)
            else:
                active_neighbors.add(n)

        next_active_neighbors = set()
        next_inactive_neighbors = set()

        num_active = 0
        for n in active_neighbors:
            nbs = get_neighbors(n)
            for nextn in nbs:
                if nextn in already_checked:
                    continue
                if nextn.z not in node:
                    node[nextn.z] = dict()
                if nextn.y not in node[nextn.z]:
                    node[nextn.z][nextn.y] = set()
                if nextn.x not in node[nextn.z][nextn.y]:
                    continue
                else:
                    num_active += 1
            already_checked.add(n)
            if num_active in {2,3}:
                next_active_neighbors.add(n)
            else:
                next_inactive_neighbors.add(n)

        num_active = 0
        for n in inactive_neighbors:
            nbs = get_neighbors(n)
            for nextn in nbs:
                if nextn in already_checked:
                    continue
                if nextn.z not in node:
                    node[nextn.z] = dict()
                if nextn.y not in node[nextn.z]:
                    node[nextn.z][nextn.y] = set()
                if nextn.x not in node[nextn.z][nextn.y]:
                    continue
                else:
                    num_active += 1
            already_checked.add(n)
            if num_active == 3:
                next_active_neighbors.add(n)
            else:
                next_inactive_neighbors.add(n)

        already_checked.add(c)

        if active:
            if len(active_neighbors) in {2,3}:
                next_active_neighbors.add(c)
            else:
                next_inactive_neighbors.add(c)
        else:
            if len(active_neighbors) == 3:
                next_active_neighbors.add(c)
            else:
                next_inactive_neighbors.add(c)

        return already_checked, next_active_neighbors, next_inactive_neighbors




    cycle = 1
    while cycle < 7:
        next_active = set()
        next_inactive = set()
        already_checked = set()

        for c in active_nodes:
            checked,na,ni = process_neighbors(c, True, already_checked)
            already_checked.update(checked)
            next_active.update(na)
            next_inactive.update(ni)

        for n in next_active:
            node[n.z][n.y].add(n.x)

        for n in next_inactive:
            node[n.z][n.y].discard(n.x)

        active_nodes = next_active
        cycle += 1

    print(len(active_nodes))
