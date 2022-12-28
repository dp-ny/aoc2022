from datetime import datetime

test_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

DEBUG = True
debug = print if DEBUG else lambda _: _


def parse_rocks(input):
    rocks = []
    for part in input:
        parts = part.split(" -> ")
        for i in range(len(parts) - 1):
            start = [int(n) for n in parts[i].split(",")]
            end = [int(n) for n in parts[i + 1].split(",")]
            x_dir = 1 if end[0] >= start[0] else -1
            y_dir = 1 if end[1] >= start[1] else -1
            for x in range(start[0], end[0] + x_dir, x_dir):
                for y in range(start[1], end[1] + y_dir, y_dir):
                    rocks.append((x, y))
    return rocks

def print_grid(start, rocks, sands, min_p = None, max_p = None):
    all_points = rocks + sands + [start]
    if min_p is None:
        min_x = min([point[0] for point in all_points])
        min_y = min([point[1] for point in all_points])
        min_p = (min_x, min_y)
    if max_p is None:
        max_x = max([point[0] for point in all_points])
        max_y = max([point[1] for point in all_points])
        max_p = (max_x, max_y)
    
    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x, max_x + 1):
            if (x, y) == start:
                line += '+'
            elif (x, y) in rocks:
                line += '#'
            elif (x, y) in sands:
                line += 'O'
            else:
                line += '.'
        debug(line)

    pass

start = (500, 0)
def part1(input):
    # input = test_input.split("\n")
    now = datetime.now()
    rocks = parse_rocks(input)
    max_rock_y = max([p[1] for p in rocks])
    sands = []

    print("done with init", datetime.now() - now)

    # fns for placing sand
    blocked = set(rocks + sands)
    get_spots = lambda p: [(p[0], p[1] + 1), (p[0] - 1, p[1] + 1), (p[0] + 1, p[1] + 1)]

    print_all = lambda: print_grid(start, rocks, sands) if False else start

    debug("====START====")
    print_all()

    new_sand = start
    count = 1
    now = datetime.now()
    checks = 0
    while new_sand[1] < max_rock_y:
        
        # find available spot
        available_spot = next((p for p in get_spots(new_sand) if p not in blocked), None)
        if count % 100 == 0:
            print("checking new_sand", new_sand, f"Spots: ({available_spot})", f"using: {available_spot}")

        # if there's none, that sand is placed
        if available_spot is None:
            sands.append(new_sand)
            blocked.add(new_sand)
            new_sand = start
            debug(f"====Sand {count}====")
            print_all()
            debug(f"====Sand {count}==== {checks} {datetime.now() - now}")
            count += 1
            checks = 0
            now = datetime.now()
        else:
            # else continue dropping sand
            checks += 1
            new_sand = available_spot


    debug("====DONE====")
    print_all()

    print("count", count - 1)
    print("sands", len(sands), sands)


def part2(input):
    # input = test_input.split("\n")
    now = datetime.now()
    rocks = parse_rocks(input)
    max_rock_y = max([p[1] for p in rocks])

    sands = []

    print("done with init", datetime.now() - now)

    # fns for placing sand
    blocked = set(rocks + sands)
    get_spots = lambda p: [(p[0], p[1] + 1), (p[0] - 1, p[1] + 1), (p[0] + 1, p[1] + 1)]

    def print_all(force = False):
        print_grid(start, rocks, sands) if force else start

    debug("====START====")
    print_all()

    new_sand = start
    count = 1
    now = datetime.now()
    checks = 0
    while True:
        
        # find available spot
        is_blocked = lambda p: p in blocked or p[1] >= max_rock_y + 2
        available_spot = next((p for p in get_spots(new_sand) if not is_blocked(p)), None)

        # if there's none, that sand is placed
        if available_spot is None:
            if new_sand == start:
                break
            sands.append(new_sand)
            blocked.add(new_sand)
            new_sand = start
            debug(f"====Sand {count}====")
            print_all()
            debug(f"====Sand {count}==== {checks} {datetime.now() - now}")
            count += 1
            checks = 0
            now = datetime.now()
        else:
            # else continue dropping sand
            checks += 1
            new_sand = available_spot


    debug("====DONE====")
    print_all(True)

    print("sands", len(sands), sands)
    print("count", count - 1)
