from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def move_left(self):
        return Point(self.x - 1, self.y)
    def move_right(self):
        return Point(self.x + 1, self.y)
    def move_up(self):
        return Point(self.x, self.y - 1)
    def move_down(self):
        return Point(self.x, self.y + 1)

    def tuple(self):
        return (self.x, self.y)

    def is_adjacent(self, other):
        return self.x - 1 <= other.x and  other.x <= self.x + 1\
            and self.y - 1 <= other.y and other.y <= self.y + 1
        
testInput = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

testInput2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
def part1(input):
    # input = testInput.split('\n')
    moves = input

    # start = Point(0, 0)
    h_pos = Point(0, 0)
    t_pos = Point(0, 0)
    t_visited = set([(0,0)])
    for move in moves:
        parts = move.split(" ")
        dir = parts[0]
        length = int(parts[1])
        # do moves
        for _ in range(0, length):
            move_point = {
                "U": lambda p: p.move_up(),
                "R": lambda p: p.move_right(),
                "D": lambda p: p.move_down(),
                "L": lambda p: p.move_left(),
            }[dir]
            h_pos = move_point(h_pos)
            if h_pos.is_adjacent(t_pos):
                continue
            if not (t_pos.x == h_pos.x or t_pos.y == h_pos.y):
                if t_pos.x + 1 == h_pos.x:
                    t_pos = t_pos.move_right()
                elif t_pos.x - 1 == h_pos.x:
                    t_pos = t_pos.move_left()
                elif t_pos.y + 1 == h_pos.y:
                    t_pos = t_pos.move_down()
                elif t_pos.y - 1 == h_pos.y:
                    t_pos = t_pos.move_up()
            # always move t same way that h moved
            t_pos = move_point(t_pos)
            print(t_pos)
            t_visited.add(t_pos.tuple())
    
    min_x = min([0] + list(map(lambda p: p[0], t_visited)))
    max_x = max(list(map(lambda p: p[0], t_visited)))
    min_y = min([0] + list(map(lambda p: p[1], t_visited)))
    max_y = max(list(map(lambda p: p[1], t_visited)))

    for y in range(min_y, max_y + 1):
        line = []
        for x in range(min_x, max_x + 1):
            if x == 0 and y == 0:
                line.append('s')
                continue
            if (x, y) in t_visited:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))

    print(len(t_visited))

def part2(file_input):
    # input = testInput2.split('\n')
    moves = file_input

    def move_tail(curr, prev, shouldPrint = False):
        if curr.is_adjacent(prev):
            if shouldPrint: print('is_adjacent', curr, prev)
            return prev
        if not (prev.x == curr.x or prev.y == curr.y):
            if shouldPrint: print('moving diag')
            if prev.x + 1 == curr.x:
                prev = prev.move_right()
            elif prev.x - 1 == curr.x:
                prev = prev.move_left()
            elif prev.y + 1 == curr.y:
                prev = prev.move_down()
            elif prev.y - 1 == curr.y:
                prev = prev.move_up()

        if shouldPrint: print ('doing normal move')
        if prev.x + 2 == curr.x:
            prev = prev.move_right()
        if prev.x - 2 == curr.x:
            prev = prev.move_left()
        if prev.y + 2 == curr.y:
            prev = prev.move_down()
        if prev.y - 2 == curr.y:
            prev = prev.move_up()
        # always move t same way that h moved
        return prev


    # start = Point(0, 0)
    knots = [Point(0,0) for _ in range(0, 10)]
    t_visited = set([(0,0)])
    min_x = lambda: min([0] + list(map(lambda p: p[0], t_visited)) + list(map(lambda p: p.x, knots)))
    max_x = lambda: max(list(map(lambda p: p[0], t_visited)) + list(map(lambda p: p.x, knots)))
    min_y = lambda: min([0] + list(map(lambda p: p[1], t_visited)) + list(map(lambda p: p.y, knots)))
    max_y = lambda: max(list(map(lambda p: p[1], t_visited)) + list(map(lambda p: p.y, knots)))

    def print_visited(min_x, max_x, min_y, max_y, knots):
        for y in range(min_y, max_y + 1):
            line = []
            for x in range(min_x, max_x + 1):
                if x == 0 and y == 0:
                    line.append('s')
                    continue
                p = None
                try:
                    p = knots.index((x, y))
                except:
                    pass
                if p is not None:
                    line.append(str(p))
                    continue
                if (x, y) in t_visited:
                    line.append('#')
                else:
                    line.append('.')
            print(str(y).ljust(5, ' '), ''.join(line))

    index = 0
    for move in moves:
        print(f'{index} {move}------------------')
        parts = move.split(" ")
        dir = parts[0]
        length = int(parts[1])
        # do moves
        for _ in range(0, length):
            move_point = {
                "U": lambda p: p.move_up(),
                "R": lambda p: p.move_right(),
                "D": lambda p: p.move_down(),
                "L": lambda p: p.move_left(),
            }[dir]
            knots[0] = move_point(knots[0])

            for i in range(0, len(knots) - 1):
                shouldPrint = index == 121 and _ == 2
                if shouldPrint:
                    print(i+1, '******')
                prev = move_tail(knots[i], knots[i + 1], shouldPrint)
                if shouldPrint:
                    print(f'{i + 1}: moving {knots[i]}, {knots[i + 1]} => {prev}')
                knots[i+1] = prev
            # print(knots)
            # track last knot
            # print(knots[-1])
            t_visited.add(knots[-1].tuple())
            # print(move, '______', _)
        # print(knots)
            # print_visited(min_x(), max_x(), min_y(), max_y(), list(map(lambda p: (p.x, p.y), knots)))
        index += 1
        # if index > 121:
        #     # _ = input('wait until ready\n')
        #     break
        
    print('endzzzzzzzzzzzzzz')
    print_visited(min_x(), max_x(), min_y(), max_y(), list(map(lambda p: (p.x, p.y), knots)))
    print(knots)

    print(len(t_visited))
