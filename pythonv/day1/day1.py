with open("input1.txt", "r") as f:
    calories = []
    curr_cals = 0
    for row in f.readlines():
        row = row.replace("\n", "")
        if (row == ''):
            calories.append(curr_cals)
            curr_cals = 0
            continue
        curr_cals = curr_cals + int(row)

    print(calories)
    first = max(calories)
    calories.remove(first)
    second = max(calories)
    calories.remove(second)
    third = max(calories)
    print(first, second, third, sum([first, second, third]))


