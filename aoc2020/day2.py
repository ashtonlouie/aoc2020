from collections import Counter, namedtuple

if __name__ == "__main__":

    Data = namedtuple('Data', ['low', 'high', 'char', 'pw'])
    with open('data/input2.txt') as f:
        input = f.readlines()
        data = set()
        for x in input:
            entries = x.split(' ')
            low = int(entries[0].split('-')[0])
            high = int(entries[0].split('-')[1])
            char = entries[1][0]
            pw = entries[2][:-1]
            d = Data(low, high, char, pw)
            data.add(d)


    ## part 1
    valid = 0
    for d in data:
        c = Counter(d.pw)
        if c[d.char] >= d.low and c[d.char] <= d.high:
            valid += 1

    print(valid)

    ## part 2
    valid = 0
    for d in data:
        if d.pw[d.low-1] == d.char:
            if d.pw[d.high-1] != d.char:
                valid += 1
        elif d.pw[d.high-1] == d.char:
            valid += 1

    print(valid)
