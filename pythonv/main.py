import argparse
import os
import importlib

parser = argparse.ArgumentParser()

parser.add_argument('--day', help='This is day to run')
parser.add_argument('--part', help='This is the part to run')

# Parse the arguments
args = parser.parse_args()

# Check if the flags were provided
if not args.day or not args.part:
    print('One or more flags were not provided')
    exit()

day = int(args.day)
part = int(args.part)

if part != 1 and part != 2:
    print(f'part must be 1 or 2, but was {part}')
    exit()

day_path = f'day{day}/day{day}.py'
if not os.path.exists(day_path):
    print(f'unable to find day {day}')
    exit()

input_path = f'day{day}/input.txt'
if not os.path.exists(input_path):
    print(f'unable to find input for {day}')
    exit()

if day < 6:
    print("can't use for days < 6")
    exit()

module_name = f'day{day}.day{day}'
day_module = importlib.import_module(module_name)
if not day_module:
    print('unable to load module')
    print(module_name)
    exit()

if (part == 1 and not hasattr(day_module, 'part1')) or (part == 2 and not hasattr(day_module, 'part2')):
    print(f'unable to find expected part {part} in day{day}')
    exit()

def run():
    if part == 1:
        day_module.part1(input)
    if part == 2:
        day_module.part2(input)

with open(input_path, 'r') as f:
    input = f.read().split('\n')
    run()