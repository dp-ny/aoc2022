import math
import json
import functools

test_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

def parse_input(input):
    offset = 3
    pairs = []
    for i in range(math.floor(len(input)/ 3) + 1):
        base = offset * i
        left = json.loads(input[base])
        right = json.loads(input[base + 1])
        pairs.append((left, right))
    return pairs

def compare(left, right):
    debug = print
    # debug = lambda s: s
    debug(f' - Compare {left} vs {right}')
    if type(left) is int and type(right) is int:
        # handle both int
        if left < right:
            debug('    left < right: True')
            return True
        if right < left:
            debug('    right < left: True')
            return False
        return None

    elif not type(left) is list:
        debug(f'Mixed types; convert left to [{left}] and retry comparison')
        left = [left]
        debug(f' - Compare {left} vs {right}')
    elif not type(right) is list:
        debug(f'Mixed types; convert right to [{right}] and retry comparison')
        right = [right]
        debug(f' - Compare {left} vs {right}')

    # both lists
    assert type(left) is list and type(right) is list

    longer_len = max(len(left), len(right))
    for i in range(longer_len):
        if i >= len(left):
            debug('    left ran out: True')
            return True
        if i >= len(right):
            debug('    right ran out: False')
            return False
        result = compare(left[i], right[i])
        if result is not None:
            return result
    return None

def part1(input):
    # input = test_input.split("\n")
    pairs = parse_input(input)
    count = 1
    correct_pair_indexes = []
    for pair in pairs:
        print(f"=========Pair {count}============")
        left, right = pair
        result = compare(left, right)
        assert result is not None
        if result:
            print(f"Result {left} to {right} = {result}\n\n")
            correct_pair_indexes.append(count)
        count += 1

    print(correct_pair_indexes)
    print(sum(correct_pair_indexes))

def part2(input):
    parts = parse_input(input)
    pairs = [left for left, _ in parts] + [right for _, right in parts] + [[[2]], [[6]]]

    cmp_func = lambda left, right: 1 if compare(left, right) else -1

    sorted_pairs = sorted(pairs, key=functools.cmp_to_key(cmp_func))
    
    index1 = sorted_pairs.index([[2]])
    index2 = sorted_pairs.index([[6]])
    
    print(sorted_pairs)
    print(index1, index2, index1 * index2)