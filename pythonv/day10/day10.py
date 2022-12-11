testInput = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

def calc_register_vals(input):
    cycle = 0
    registers = {
        "x": 1,
    }
    register_vals = {}
    def inc_cycle(instruction):
        nonlocal cycle
        cycle += 1    
        register_vals[cycle] = registers["x"]
        # print(cycle, "-", "x:", registers["x"], "----", instruction)

    for instruction in input:
        inc_cycle(instruction)
        parts = instruction.split(' ')
        if parts[0] == "noop":
            continue
        if parts[0] == "addx":
            inc_cycle(instruction)
            registers["x"] += int(parts[1])
    
    register_vals[cycle] = registers["x"]
    return register_vals


def part1(input):
    # input = testInput.split('\n')
    register_vals = calc_register_vals(input)

    print(register_vals)
    vals = [20, 60, 100, 140, 180, 220]
    sum = 0
    for val in vals:
        p = val * register_vals[val]
        print(val, ":", register_vals[val], p)
        sum += p
                

width = 40
height = 6
def part2(input):
    register_vals = calc_register_vals(input)
    print(register_vals)
    line = []
    for cycle in range(1, len(register_vals) + 1):
        if len(line) == 40:
            print(''.join(line))
            line = []
        val = register_vals[cycle]
        display_pixels = [val - 1, val, val + 1]
        # print(cycle, "or", len(line) + 1, "in", display_pixels)
        if len(line) in display_pixels:
            line.append('#')
        else:
            line.append('.')
    print(''.join(line))
    print('done')