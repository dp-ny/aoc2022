def parse_grid(input):
    grid = [list(line) for line in input]
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == 'S':
                start = (x, y)
            if grid[y][x] == 'E':
                end = (x, y)
    return (grid, start, end)

def valid_move(grid, curr, other):
    curr_val = grid[curr[1]][curr[0]]
    if curr_val == 'S':
        curr_val = 'a'
    if curr_val == 'E':
        curr_val = 'z'
    other_val = grid[other[1]][other[0]]
    if other_val == 'S':
        other_val = 'a'
    if other_val == 'E':
        other_val = 'z'

    result = ord(curr_val) - 1 <= ord(other_val)
    print('comparing', curr_val, ord(curr_val), other_val, ord(other_val), result)
    return result


def get_adj(grid, curr):
    x, y = curr
    adj = []
    if x - 1 >= 0:
        p = (x-1, y)
        adj.append(p)
    if x + 1 < len(grid[0]):
        p = (x+1, y)
        adj.append(p)
    if y - 1 >= 0:
        p = (x, y-1)
        adj.append(p)
    if y + 1 < len(grid):
        p = (x, y+1)
        adj.append(p)
    return adj

def part1(input):
    grid, start, end = parse_grid(input)
    print("size:", len(grid[0]), len(grid))

    parents = {}
    visited = set()
    visited.add(start)
    parents[start] = None
    queue = [start]
    while len(queue) > 0:
        curr = queue.pop()
        curr_val = grid[curr[1]][curr[0]]
        if curr == end:
            break
        adj_cells = get_adj(grid, curr)
        for adj in adj_cells:
            if adj in visited:
                continue
            if valid_move(grid, adj, curr):
                visited.add(adj)
                parents[adj] = curr
                queue.insert(0, adj)
    
    print('visited---------------')
    for y in range(0, len(grid)):
        line = []
        for x in range(0, len(grid[0])):
            if (x, y) in visited:
                line.append('#')
            else:
                line.append(grid[y][x])
        print(''.join(line))

    curr = end
    count = 0
    while curr is not None:
        print(curr)
        count += 1
        curr = parents[curr]
    print("count:", count)

def part2(input):
    grid, start, end = parse_grid(input)
    print("size:", len(grid[0]), len(grid))

    parents = {}
    visited = set()
    visited.add(end)
    parents[end] = None
    queue = [end]
    low = None
    while len(queue) > 0:
        curr = queue.pop()
        curr_val = grid[curr[1]][curr[0]]
        if curr_val == 'a':
            low = curr
            print('low is', low)
            break
        adj_cells = get_adj(grid, curr)
        for adj in adj_cells:
            if adj in visited:
                continue
            if valid_move(grid, curr, adj):
                visited.add(adj)
                parents[adj] = curr
                queue.insert(0, adj)
    
    print('visited---------------')
    for y in range(0, len(grid)):
        line = []
        for x in range(0, len(grid[0])):
            if (x, y) in visited:
                line.append('#')
            else:
                line.append(grid[y][x])
        print(''.join(line))

    curr = low
    count = 0
    while curr is not None:
        print(curr)
        count += 1
        curr = parents[curr]
    print("count:", count)