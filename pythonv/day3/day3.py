def score_letter(letter):
    ordinality = ord(letter)
    if ordinality >= ord('a'):
        return ordinality - ord('a') + 1
    return ordinality - ord('A') + 27

def part1():
    with open("day3/input.txt", "r") as f:
        lines = f.readlines()
        dupes = []
        for line in lines:
            line = line.replace('\n', '')
            parts = list(line)
            mid = int(len(parts) / 2)
            # dedup left and right
            parts = list(set(parts[:mid])) + list(set(parts[mid:]))
            parts.sort()
            for i in range(0, len(parts) - 1):
                if parts[i] == parts[i+1]:
                    dupes.append(parts[i])
                    break
        
        scores = list(map(score_letter, dupes))
        total = sum(scores)
        print(dupes)
        print(scores)
        print(total)

def part2():
    with open("day3/input.txt", "r") as f:
        lines = f.readlines()
        dupes = []
        curr_group = []
        group_index = 0
        for line in lines:
            group_index += 1

            line = line.replace('\n', '')
            parts = list(line)
            parts = list(set(parts))
            curr_group += parts

            if group_index < 3:
                continue
            group_index = 0
            curr_group.sort()

            for i in range(0, len(curr_group) - 2):
                if curr_group[i] == curr_group[i+1] and curr_group[i+1] == curr_group[i+2]:
                    dupes.append(curr_group[i])
                    break
            curr_group = []
        
        scores = list(map(score_letter, dupes))
        total = sum(scores)
        print(dupes)
        print(scores)
        print(total)
        
part2()
