my_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

result_score = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

score_results = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}

my_move = {
    "A X": 'Z',
    "A Y": 'X',
    "A Z": 'Y',
    "B X": 'X',
    "B Y": 'Y',
    "B Z": 'Z',
    "C X": 'Y',
    "C Y": 'Z',
    "C Z": 'X',
}

def part1():
    with open("day2/input.txt", "r") as f:
        # games = ["A Y\n", "B X\n", "C Z\n"]
        games = f.readlines()
        scores = []
        for line in games:
            game = line.replace("\n", "")
            parts = game.split(" ")
            theirs = parts[0]
            mine = parts[1]

            game_score = my_score[mine] + score_results[game]
            scores.append(game_score)
        print(scores)
        print(sum(scores))

def part2():
    with open("day2/input.txt", "r") as f:
        # games = ["A Y\n", "B X\n", "C Z\n"]
        games = f.readlines()
        scores = []
        for line in games:
            game = line.replace("\n", "")
            parts = game.split(" ")
            theirs = parts[0]
            result = parts[1]
            mine = my_move[game]

            game_score = my_score[mine] + result_score[result]
            scores.append(game_score)
        print(scores)
        print(sum(scores))

part2()