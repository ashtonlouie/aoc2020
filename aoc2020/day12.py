from collections import Counter, namedtuple, OrderedDict, deque
from typing import Set, Dict, List, Deque
from functools import reduce
import re

if __name__ == "__main__":

    with open('data/input12.txt') as f:
        data = f.read().splitlines()

    Command = namedtuple('Command', ['cmd', 'val'])

    commands = list()
    for d in data:
        commands.append(Command(d[:1], int(d[1:])))

    x = 0
    y = 0

    # 0 == east, 90 == north, 180 == west, 270 == south
    direction = 0

    for c in commands:
        if c.cmd == 'N':
            y += c.val
        elif c.cmd == 'S':
            y -= c.val
        elif c.cmd == 'E':
            x += c.val
        elif c.cmd == 'W':
            x -= c.val
        elif c.cmd == 'L':
            direction += c.val
            if direction >= 360:
                direction -= 360
        elif c.cmd == 'R':
            direction -= c.val
            if direction < 0:
                direction += 360
        elif c.cmd == 'F':
            if direction == 0:
                x += c.val
            elif direction == 90:
                y += c.val
            elif direction == 180:
                x -= c.val
            elif direction == 270:
                y -= c.val

    # part 1

    print(abs(x) + abs(y))

    # part 2

    x = 0
    y = 0
    wx = 10
    wy = 1

    for c in commands:
        if c.cmd == 'N':
            wy += c.val
        elif c.cmd == 'S':
            wy -= c.val
        elif c.cmd == 'E':
            wx += c.val
        elif c.cmd == 'W':
            wx -= c.val
        elif c.cmd == 'L':
            if c.val == 90:
                next_wx = -wy
                next_wy = wx
            elif c.val == 180:
                next_wx = -wx
                next_wy = -wy
            elif c.val == 270:
                next_wx = wy
                next_wy = -wx
            wx = next_wx
            wy = next_wy
        elif c.cmd == 'R':
            if c.val == 90:
                next_wx = wy
                next_wy = -wx
            elif c.val == 180:
                next_wx = -wx
                next_wy = -wy
            elif c.val == 270:
                next_wx = -wy
                next_wy = wx
            wx = next_wx
            wy = next_wy
        elif c.cmd == 'F':
            x += wx * c.val
            y += wy * c.val

    print(abs(x) + abs(y))

