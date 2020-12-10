from collections import Counter, namedtuple

if __name__ == "__main__":

    Data = namedtuple('Data', ['low', 'high', 'char', 'pw'])
    with open('data/input03.txt') as f:
        input = f.read().splitlines()

    ## part 1
    def part1(delx, dely):
        x = 0
        y = 0
        width = len(input[0])
        trees = 0
        while y < len(input) - dely:
            y += dely
            x = x + delx if (x + delx < width) else x + delx - width
            if input[y][x] == '#':
                trees += 1

        return trees

    print(part1(3,1))

    ## part 2
    print(part1(1,1) * part1(3,1) * part1(5,1) * part1(7,1) * part1(1,2))