from dataclasses import dataclass

def parse_grid(input):
    return [list(map(lambda c: int(c), list(line))) for line in input]

@dataclass
class OrdMaxes:
    up: int = None
    down: int = None
    left: int = None
    right: int = None

    def is_visible(self, height):
        return height > self.up or height > self.down\
            or height > self.left or height > self.right
    
    def prod(self):
        if None in [self.up, self.down, self.left, self.right]:
            return 0
        return self.up * self.down * self.left * self.right

def part1(input):
    grid = parse_grid(input)

    grid_maxes = [[OrdMaxes() for x in range(0, len(grid[0]))] for y in range(0, len(grid))]
    for y in range(0, len(grid)):
        max_x = -1
        max_y = -1
        for x in range(0, len(grid[0])):
            grid_maxes[y][x].left = max_x
            curr_x = grid[y][x]
            max_x = max([max_x, curr_x])

            grid_maxes[x][y].up = max_y
            curr_y = grid[x][y]
            max_y = max([max_y, curr_y])

        max_x = -1
        max_y = -1
        for x in range(len(grid[0]) - 1, -1, -1):
            grid_maxes[y][x].right = max_x
            max_x = max([max_x, grid[y][x]])

            grid_maxes[x][y].down = max_y
            max_y = max([max_y, grid[x][y]])

    visible_cells = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid_maxes[y][x].is_visible(grid[y][x]):
                visible_cells.append((x, y))
    print(visible_cells)
    print(len(visible_cells))

testInput = """30373
25512
65332
33549
35390"""

def part2(input):
    # input = testInput.split('\n')
    grid = parse_grid(input)
    grid_maxes = [[OrdMaxes() for x in range(0, len(grid[0]))] for y in range(0, len(grid))]

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            curr = grid[y][x]
            x_count = 0
            for backtrack in range(x - 1, -1, -1):
                x_count += 1
                if x == 14 and y == 52:
                    print("left", backtrack, grid[y][backtrack], curr, x_count, grid_maxes[y][x].left)
                if grid_maxes[y][x].left is None and grid[y][backtrack] >= curr:
                    grid_maxes[y][x].left = x_count
            if grid_maxes[y][x].left is None:
                grid_maxes[y][x].left = x_count

            y_count = 0
            for backtrack in range(y - 1, -1, -1):
                y_count += 1
                if x == 14 and y == 52:
                    print("up", backtrack, grid[backtrack][x], curr, y_count, grid_maxes[y][x].up)
                if grid_maxes[y][x].up is None and grid[backtrack][x] >= curr:
                    grid_maxes[y][x].up = y_count
            if grid_maxes[y][x].up is None:
                grid_maxes[y][x].up = y_count

        for x in range(len(grid[0]) - 1, -1, -1):
            curr = grid[y][x]
            x_count = 0
            for backtrack in range(x + 1, len(grid[0])):
                x_count += 1
                if x == 14 and y == 52:
                    print("right", backtrack, grid[y][backtrack], curr, x_count, grid_maxes[y][x].right)
                if grid_maxes[y][x].right is None and grid[y][backtrack] >= curr:
                    grid_maxes[y][x].right = x_count
            if grid_maxes[y][x].right is None:
                grid_maxes[y][x].right = x_count

            y_count = 0
            for backtrack in range(y + 1, len(grid)):
                y_count += 1
                if x == 14 and y == 52:
                    print("down", backtrack, grid[backtrack][x], curr, y_count, grid_maxes[y][x].down)
                if grid_maxes[y][x].down is None and grid[backtrack][x] >= curr:
                    grid_maxes[y][x].down = y_count
            if grid_maxes[y][x].down is None:
                grid_maxes[y][x].down = y_count

    total = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid_maxes[y][x].prod() > total:
                print('x', x, 'y', y)
            total = max([grid_maxes[y][x].prod(), total])

    # for m in grid_maxes: print(m)
    print (grid_maxes[52][14])
    print(total)


