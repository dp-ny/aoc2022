def find_first_marker(buff, sop_marker_length):
    for i in range(0, len(buff) - sop_marker_length):
        test_str = set(buff[i:i+sop_marker_length])
        if len(test_str) == sop_marker_length:
            break

    print('result:', i + sop_marker_length)


def part1(input):
    assert len(input) == 1
    buff = input[0]
    find_first_marker(buff, 4)

def part2(input):
    assert len(input) == 1
    buff = input[0]
    find_first_marker(buff, 14)
