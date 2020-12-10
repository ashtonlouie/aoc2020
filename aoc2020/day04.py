from collections import Counter, namedtuple, OrderedDict
from typing import Set
import re

if __name__ == "__main__":

    passports = set()

    valid = 0
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    with open('data/input04.txt') as f:
        data = f.read().splitlines()

    # part 1

    # passport = set()
    # for i in range(len(data)):
    #     line = data[i]
    #     if not line:
    #         if required.issubset(passport):
    #             valid += 1
    #         passport = set()
    #         continue
    #
    #     kv = line.split(' ')
    #     for x in kv:
    #         key = x.split(':')[0]
    #         passport.add(key)
    #
    #     if i == len(data) - 1:
    #         if required.issubset(passport):
    #             valid += 1
    #         passport = set()
    #
    # print(valid)

    ## part 2

    def validate(passport) -> bool:
        if 'byr' in passport:
            if len(passport['byr']) != 4 or int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
                return False
        else:
            return False

        if 'iyr' in passport:
            if len(passport['iyr']) != 4 or int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
                return False
        else:
            return False

        if 'eyr' in passport:
            if len(passport['eyr']) != 4 or int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
                return False
        else:
            return False

        if 'hgt' in passport:
            hgt = passport['hgt']
            if not re.match(r'^[0-9]{2,3}(cm|in)$', hgt):
                return False
            unit = hgt[-2:]
            value = int(hgt[:-2])
            if unit == 'cm':
                if value < 150 or value > 193:
                    return False
            elif unit == 'in':
                if value < 59 or value > 76:
                    return False
        else:
            return False

        if 'hcl' in passport:
            if not re.match(r'^#[a-f0-9]{6}', passport['hcl']):
                return False
        else:
            return False

        if 'ecl' in passport:
            valid_ecl = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
            if passport['ecl'] not in valid_ecl:
                return False
        else:
            return False

        if 'pid' in passport:
            if not re.match(r'^[0-9]{9}$', passport['pid']):
                return False
        else:
            return False

        return True


    passport = dict()
    for i in range(len(data)):
        line = data[i]
        if not line:
            if validate(passport):
                valid += 1
            passport = dict()
            continue

        kv = line.split(' ')
        for x in kv:
            pair = x.split(':')
            key = pair[0]
            value = pair[1]
            passport[key] = value

        if i == len(data) - 1:
            if validate(passport):
                valid += 1
            passport = dict()

    print(valid)

