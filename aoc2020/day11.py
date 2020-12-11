from collections import Counter, namedtuple, OrderedDict, deque
from typing import Set, Dict, List, Deque
from functools import reduce
import re

if __name__ == "__main__":

    with open('data/input11.txt') as f:
        data = f.read().splitlines()

    h = len(data)
    w = len(data[0])

    # part 1

    occupied = set()
    unoccupied = set()

    for i in range(h):
        for j in range(w):
            if data[i][j] == 'L':
                unoccupied.add((i, j))

    # placeholder
    changed = len(unoccupied)

    while changed > 0:
        changed = 0
        next_occupied = set()
        next_unoccupied = set()
        for row, col in unoccupied:
            will_change = True
            if row - 1 >= 0:
                if col - 1 >= 0:
                    if (row - 1, col - 1) in occupied:
                        will_change = False
                if col + 1 < w and will_change:
                    if (row - 1, col + 1) in occupied:
                        will_change = False
                if (row - 1, col) in occupied and will_change:
                    will_change = False

            if row + 1 < h and will_change:
                if col - 1 >= 0:
                    if (row + 1, col - 1) in occupied:
                        will_change = False
                if col + 1 < w and will_change:
                    if (row + 1, col + 1) in occupied:
                        will_change = False
                if (row + 1, col) in occupied and will_change:
                    will_change = False

            if col - 1 >= 0 and will_change:
                if (row, col - 1) in occupied:
                    will_change = False
            if col + 1 < w and will_change:
                if (row, col + 1) in occupied:
                    will_change = False

            if will_change:
                next_occupied.add((row, col))
                changed += 1
            else:
                next_unoccupied.add((row, col))

        for row, col in occupied:
            adjacent = 0
            if row - 1 >= 0:
                if col - 1 >= 0:
                    if (row - 1, col - 1) in occupied:
                        adjacent += 1
                if col + 1 < w:
                    if (row - 1, col + 1) in occupied:
                        adjacent += 1
                if (row - 1, col) in occupied:
                    adjacent += 1

            if row + 1 < h:
                if col - 1 >= 0:
                    if (row + 1, col - 1) in occupied:
                        adjacent += 1
                if col + 1 < w:
                    if (row + 1, col + 1) in occupied:
                        adjacent += 1
                if (row + 1, col) in occupied:
                    adjacent += 1

            if col - 1 >= 0:
                if (row, col - 1) in occupied:
                    adjacent += 1
            if col + 1 < w:
                if (row, col + 1) in occupied:
                    adjacent += 1

            if adjacent >= 4:
                next_unoccupied.add((row, col))
                changed += 1
            else:
                next_occupied.add((row, col))

        occupied = next_occupied
        unoccupied = next_unoccupied

    print(len(occupied))

    # part 2

    occupied = set()
    unoccupied = set()

    for i in range(h):
        for j in range(w):
            if data[i][j] == 'L':
                unoccupied.add((i, j))

    # placeholder
    changed = len(unoccupied)

    while changed > 0:
        changed = 0
        next_occupied = set()
        next_unoccupied = set()
        for row, col in unoccupied:
            will_change = True

            # look up
            for y in range(row - 1, -1, -1):
                if (y, col) in occupied:
                    will_change = False
                    break
                if (y, col) in unoccupied:
                    break

            # look down
            if will_change:
                for y in range(row + 1, h):
                    if (y, col) in occupied:
                        will_change = False
                        break
                    if (y, col) in unoccupied:
                        break

            # look left
            if will_change:
                for x in range(col - 1, -1, -1):
                    if (row, x) in occupied:
                        will_change = False
                        break
                    if (row, x) in unoccupied:
                        break

            # look right
            if will_change:
                for x in range(col + 1, w):
                    if (row, x) in occupied:
                        will_change = False
                        break
                    if (row, x) in unoccupied:
                        break

            # look up left
            if will_change:
                y = row - 1
                x = col - 1
                while x >= 0 and y >= 0:
                    if (y, x) in occupied:
                        will_change = False
                        break
                    if (y, x) in unoccupied:
                        break
                    y -= 1
                    x -= 1

            # look up right
            if will_change:
                y = row - 1
                x = col + 1
                while x < w and y >= 0:
                    if (y, x) in occupied:
                        will_change = False
                        break
                    if (y, x) in unoccupied:
                        break
                    y -= 1
                    x += 1

            # look down left
            if will_change:
                y = row + 1
                x = col - 1
                while x >= 0 and y < h:
                    if (y, x) in occupied:
                        will_change = False
                        break
                    if (y, x) in unoccupied:
                        break
                    y += 1
                    x -= 1

            # look down right
            if will_change:
                y = row + 1
                x = col + 1
                while x < w and y < h:
                    if (y, x) in occupied:
                        will_change = False
                        break
                    if (y, x) in unoccupied:
                        break
                    y += 1
                    x += 1

            if will_change:
                next_occupied.add((row, col))
                changed += 1
            else:
                next_unoccupied.add((row, col))

        for row, col in occupied:
            adjacent = 0

            # look up
            for y in range(row - 1, -1, -1):
                if (y, col) in occupied:
                    adjacent += 1
                    break
                if (y, col) in unoccupied:
                    break

            # look down
            for y in range(row + 1, h):
                if (y, col) in occupied:
                    adjacent += 1
                    break
                if (y, col) in unoccupied:
                    break

            # look left
            for x in range(col - 1, -1, -1):
                if (row, x) in occupied:
                    adjacent += 1
                    break
                if (row, x) in unoccupied:
                    break

            # look right
            for x in range(col + 1, w):
                if (row, x) in occupied:
                    adjacent += 1
                    break
                if (row, x) in unoccupied:
                    break

            # look up left
            y = row - 1
            x = col - 1
            while x >= 0 and y >= 0:
                if (y, x) in occupied:
                    adjacent += 1
                    break
                if (y, x) in unoccupied:
                    break
                y -= 1
                x -= 1

            # look up right
            y = row - 1
            x = col + 1
            while x < w and y >= 0:
                if (y, x) in occupied:
                    adjacent += 1
                    break
                if (y, x) in unoccupied:
                    break
                y -= 1
                x += 1

            # look down left
            y = row + 1
            x = col - 1
            while x >= 0 and y < h:
                if (y, x) in occupied:
                    adjacent += 1
                    break
                if (y, x) in unoccupied:
                    break
                y += 1
                x -= 1

            # look down right
            y = row + 1
            x = col + 1
            while x < w and y < h:
                if (y, x) in occupied:
                    adjacent += 1
                    break
                if (y, x) in unoccupied:
                    break
                y += 1
                x += 1

            if adjacent >= 5:
                next_unoccupied.add((row, col))
                changed += 1
            else:
                next_occupied.add((row, col))

        occupied = next_occupied
        unoccupied = next_unoccupied

    print(len(occupied))