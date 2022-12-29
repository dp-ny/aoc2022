from dataclasses import dataclass
from collections import Counter

test_input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

get_distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

@dataclass
class SensorBeacon:
    sensor: tuple[int, int]
    beacon: tuple[int, int]
    distance: int

def parse_input(input):
    sensor_beacons = []
    for line in input:
        line = line.replace("Sensor at ", "")
        line = line.replace(": closest beacon is at", ",")
        parts = line.split(', ')
        sensor_x = int(parts[0].split('=')[1])
        sensor_y = int(parts[1].split('=')[1])
        beacon_x = int(parts[2].split('=')[1])
        beacon_y = int(parts[3].split('=')[1])

        sensor = (sensor_x, sensor_y)
        beacon = (beacon_x, beacon_y)
        sensor_beacons.append(SensorBeacon(sensor, beacon, get_distance(sensor, beacon)))

    return sensor_beacons

def get_adj_cells(sensor, beacon):
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    # get cells one outside range
    distance += 1
    region = []
    for i in range(distance + 1):
        j = distance - i
        for dir_x in ([1] if i == 0 else [-1, 1]):
            for dir_y in ([1] if j == 0 else [-1, 1]):
                x = sensor[0] + dir_x * i
                y = sensor[1] + dir_y * j
                if x < 0 or x > 4_000_000 or y < 0 or y > 4_000_000:
                    continue
                region.append((x, y))
    return region

def get_maxima(sensor, beacon):
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    min_x = sensor[0] - distance
    max_x = sensor[0] + distance
    min_y = sensor[1] - distance
    max_y = sensor[1] + distance
    return ([min_x, min_y], [max_x, max_y], distance)


def is_in_range(sensor, beacon, point):
    covered_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    point_distance = abs(sensor[0] - point[0]) + abs(sensor[1] - point[1])

    return point_distance <= covered_distance


def print_grid(sensor_beacons):
    sensors = [sb.sensor for sb in sensor_beacons]
    beacons = [sb.beacon for sb in sensor_beacons]
    region = []

    all_points = sensors + beacons
    min_x = min([point[0] for point in all_points])
    min_y = min([point[1] for point in all_points])
    max_x = max([point[0] for point in all_points])
    max_y = max([point[1] for point in all_points])

    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x, max_x + 1):
            p = (x, y)
            if p in sensors:
                line += 'S'
            elif p in beacons:
                line += 'B'
            elif p in region:
                line += '#'
            else:
                line += '.'
        print(line)

    

def part1(input):
    # input = test_input.split('\n')
    sensor_beacons = parse_input(input)
    # print("parsed input", sensor_beacons)

    # covered_points = []
    # for sb in sensor_beacons:
    #     print("calculating", sb, flush=True)
    #  -   region = covered_region(sb.sensor, sb.beacon)
    #     covered_points += region    
    # print("calculted regions", covered_points)
    # covered_points = set(covered_points)

    all_xs = []
    for sb in sensor_beacons:
        min_p, max_p = get_maxima(sb.sensor, sb.beacon)
        all_xs.append(min_p[0])
        all_xs.append(max_p[0])

    min_covered_x = min(all_xs)
    max_covered_x = max(all_xs)
    print(min_covered_x, "--", max_covered_x, flush=True)

    sensor_distances = [
        (sb.sensor, get_distance(sb.sensor, sb.beacon)) for sb in sensor_beacons
    ]

    y = 2_000_000
    point_in_y = set()
    count = 0
    for x in range(min_covered_x, max_covered_x + 1):
    # for x in range(0, 4_000_000):
    #     for y in range(0, 4_000_000):
            for sb in sensor_beacons:
                if is_in_range(sb.sensor, sb.beacon, (x, y)):
                    count += 1
                    break

    # print(point_in_y)
    print(len(point_in_y))
    print(count)

    # print_grid(sensor_beacons)

def part2(input):
    # input = test_input.split('\n')
    sensor_beacons = parse_input(input)
    # print("parsed input", sensor_beacons)

    # covered_points = []
    # for sb in sensor_beacons:
    #     print("calculating", sb, flush=True)
    #  -   region = covered_region(sb.sensor, sb.beacon)
    #     covered_points += region    
    # print("calculted regions", covered_points)
    # covered_points = set(covered_points)

    maximas = []
    for sb in sensor_beacons:
        min_p, max_p, distance = get_maxima(sb.sensor, sb.beacon)
        maximas.append((sb.sensor, (min_p, max_p), distance))

    # all_xs = [x for maxima in maximas for x in maxima[0]]
    # min_covered_x = min(all_xs)
    # max_covered_x = max(all_xs) 
    # print(min_covered_x, "--", max_covered_x, flush=True)

    for i in range(len(sensor_beacons)):
        sb = sensor_beacons[i]
        sensor = sb.sensor
        beacon = sb.beacon
        maxima = maximas[i][1]
        distance = maximas[i][2]
        print(f"sensor {sensor} \t beacon {beacon} \td {distance}\t covers ({maxima[0][0]}, {maxima[0][1]}) \tto ({maxima[1][0]}, {maxima[1][1]})")

    print(flush=True)
    adj_cells = {}
    for sb in sensor_beacons:
        cells = get_adj_cells(sb.sensor, sb.beacon)
        print(f"computed for sensor {sb.sensor}: {len(cells)}", flush=True)
        adj_cells[sb.sensor] = cells
    
    all_adj = [cell for cells in adj_cells.values() for cell in cells]

    print("found adj cells", len(all_adj), flush=True)

    is_in_range = lambda sensor, distance, point: get_distance(sensor, point) <= distance
    count = 0
    for point in all_adj:
        count += 1
        out_of_range = True
        for sb in sensor_beacons:
            if is_in_range(sb.sensor, sb.distance, point):
                out_of_range = False
                break
        if out_of_range:
            print("point is", point)
            print(point[0] * 4_000_000 + point[1])
            break
        pass