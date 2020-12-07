from collections import Counter, namedtuple, OrderedDict
from typing import Set, Dict
from functools import reduce
import re

if __name__ == "__main__":

    all_bags = dict()

    with open('data/input7.txt') as f:
        data = f.read().splitlines()

    for d in data:
        bag = d.split(' bags ')[0]
        inside = d.split(' contain ')[1]
        contents = dict()

        if inside == "no other bags.":
            all_bags[bag] = contents
            continue

        for b in inside.split(', '):
            num, adj, color = b.split(' ')[:-1]
            contents[f"{adj} {color}"] = int(num)

        all_bags[bag] = contents


    # part 1

    def has_shiny_gold(all_bags: Dict, bag: str, contents: Dict):
        if bag == "shiny gold":
            return True
        if not contents:
            return False
        for inner_bag in contents:
            if has_shiny_gold(all_bags, inner_bag, all_bags[inner_bag]):
                return True
        return False


    num_bags = 0

    for bag in all_bags:
        if bag == "shiny gold":
            continue
        if has_shiny_gold(all_bags, bag, all_bags[bag]):
            num_bags += 1

    print(num_bags)

    # part 2

    from operator import add
    def get_count(all_bags: Dict, bag: str, contents: Dict):
        if not contents:
            return 0
        return reduce(add, [(get_count(all_bags, b, all_bags[b]) * contents[b] + contents[b]) for b in contents])


    print(get_count(all_bags, "shiny gold", all_bags["shiny gold"]))
