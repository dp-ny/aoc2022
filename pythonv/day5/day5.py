from dataclasses import dataclass

def read_lines(day):
    f = open(f'day{day}/input.txt')
    return f.read().split('\n')

@dataclass
class Move:
    """Class for keeping track of an item in inventory."""
    count: int
    start: int
    end: int

    def from_index(self):
        return self.start - 1

    def to_index(self):
        return self.end - 1

# move 1 from 3 to 9
# move {count} from {start} to {end}
def parse_move(move: str):
    move = move.replace("move ", "")
    move = move.replace("from ", "")
    move = move.replace("to ", "")
    parts = move.split(" ")
    return Move(int(parts[0]), int(parts[1]), int(parts[2]))

def print_stacks(crates):
    for stack in crates: print(stack)

def part1():
    input = read_lines(5)

    crates = [[] for i in range(0, 9)]
    for i in range(0, 8):
        line = input[i]
        for j in range(0, 9):
            letter_index = j * 4 + 1
            letter = line[letter_index]
            if letter == ' ':
                continue
            crates[j].insert(0, letter)

    print_stacks(crates)
    for i in range(10, len(input)):
        move = parse_move(input[i])
        for _ in range(0, move.count):
            crate = crates[move.from_index()].pop()
            crates[move.to_index()].append(crate)
    print('0000000')
    print_stacks(crates)
    str = ''
    for i in range(0, 9):
        str = str + crates[i][-1]
    print(str)
            


def part2():
    input = read_lines(5)

    crates = [[] for i in range(0, 9)]
    for i in range(0, 8):
        line = input[i]
        for j in range(0, 9):
            letter_index = j * 4 + 1
            letter = line[letter_index]
            if letter == ' ':
                continue
            crates[j].insert(0, letter)

    print_stacks(crates)
    for i in range(10, len(input)):
    # num = 3
    # for i in range(10, 10 + num):
        move = parse_move(input[i])
        # get crates
        crates_to_move = crates[move.from_index()][-move.count:]
        # delete crates
        crates[move.from_index()] = crates[move.from_index()][:-move.count]
        # add crates
        crates[move.to_index()] = crates[move.to_index()] + crates_to_move
    print('0000000')
    print_stacks(crates)
    str = ''
    for i in range(0, 9):
        str = str + crates[i][-1]
    print(str)

part2()