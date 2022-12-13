from dataclasses import dataclass
from typing import Callable
from math import floor

testInput = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

@dataclass
class Monkey:
    index: int
    items: list[int]
    inspect: Callable
    next_monkey: Callable

numFields = 7

def run(input, should_decrease_worry, numRounds):
    # input = testInput.split('\n')
    numMonkeys = len(list(filter(lambda l: "Monkey" in l, input)))
    monkeys = []
    divisor_product = 1
    for m in range(0, numMonkeys):
        # parse monkey
        i = m * numFields
        index = int(input[i][-2])
        items = list(map(int, input[i+1].split(': ')[1].split(', ')))
        op_parts = input[i + 2].split(" new = ")[1].split(' ')
        print(op_parts)
        def inspect(old, op_parts = op_parts):
            first_val = old if op_parts[0] == "old" else int(op_parts[0])
            second_val = old if op_parts[2] == "old" else int(op_parts[2])
            if op_parts[1] == "+":
                return first_val + second_val
            else:
                return first_val * second_val
        test_divisor = int(input[i + 3].split(" ")[-1])
        divisor_product *= test_divisor
        true_res = int(input[i + 4].split(" ")[-1])
        false_res = int(input[i + 5].split(" ")[-1])

        def next_monkey(item, test_divisor=test_divisor, true_res=true_res, false_res=false_res):
            if item % test_divisor == 0:
                return true_res
            else:
                return false_res
        monkeys.append(Monkey(index, items, inspect, next_monkey))
    print('div product:', divisor_product)

    def print_monkey_items(i):
        for monkey in monkeys: print(f"Monkey {monkey.index}: {monkey.items}")
    
    print_monkey_items(0)

    decrease_worry = lambda item: floor(item / 3)
    inspected_item_count = [0 for _ in range(0, numMonkeys)]
    for i in range(1, numRounds + 1):
        print ("start round", i)
        for monkey in monkeys:
            print("running monkey", monkey.index)
            inspected_item_count[monkey.index] += len(monkey.items)
            for item in monkey.items:
                # print("inspecting item", item)
                # inspect
                item = monkey.inspect(item)
                # print("inspected val", item)
                # reduce
                if should_decrease_worry:
                    item = decrease_worry(item)
                else:
                    item = item % divisor_product
                # print("decreased val", item)
                # throw
                next_monkey = monkey.next_monkey(item)
                # print("next_monkey", next_monkey)
                monkeys[next_monkey].items.append(item)
            # all items thrown
            monkey.items = []
            # print_monkey_items(i)
        print(f"After round {i}, the monkeys are holding items with these worry levels:")
        for item_index in range(0, len(inspected_item_count)):
            print(item_index, ":", inspected_item_count[item_index])
        # print_monkey_items(i)
        # if i > 10:
        #     return

    print("Inspected Item Counts:")
    for i in range(0, len(inspected_item_count)):
        print(i, ":", inspected_item_count[i])

    inspected_item_count.sort()
    max1 = max(inspected_item_count)
    inspected_item_count.remove(max1)
    max2 = max(inspected_item_count)
    print (max1, max2, max1 * max2)

    


def part1(input):
    run(input, True, 20)


def part2(input):
    run(input, False, 10_000)