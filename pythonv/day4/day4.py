def read_lines():
    f = open('day4/input.txt')
    return f.read().split('\n')

def to_parts(pair):
    parts = pair.split(',')
    ass1 = parts[0].split('-')
    ass2 = parts[1].split('-')
    return ([int(ass1[0]), int(ass1[1])], [int(ass2[0]), int(ass2[1])])

def is_fully_contained(ass1, ass2):
    return ass1[0] >= ass2[0] and ass1[1] <= ass2[1]

def is_partially_contianed(ass1, ass2):
    return (ass1[0] >= ass2[0] and ass1[0] <= ass2[1])\
        or (ass1[1] >= ass2[0] and ass1[1] <= ass2[1])

test1 = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
def part1():
    input = read_lines()
    # input = test1.split('\n')
    overlapping_pairs = []
    i=0
    for pair in input:
        i+=1
        print(i)
        assignments = to_parts(pair)
        if is_fully_contained(assignments[0], assignments[1]) or is_fully_contained(assignments[1], assignments[0]):
            overlapping_pairs.append(pair)
    # for pair in overlapping_pairs: print(pair)
    print(len(overlapping_pairs))

def part2():
    input = read_lines()
    # input = test1.split('\n')
    overlapping_pairs = []
    i=0
    for pair in input:
        assignments = to_parts(pair)
        if is_partially_contianed(assignments[0], assignments[1]) or is_partially_contianed(assignments[1], assignments[0]):
            overlapping_pairs.append(pair)
    for pair in overlapping_pairs: print(pair)
    print(len(overlapping_pairs))

part2()