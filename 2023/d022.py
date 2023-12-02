import math
import re
import sys
from collections import Counter


RE_NUM_TO_COLOUR = re.compile(pattern=r'\s*(?P<num>\d+) (?P<colour>[a-z]+)')

def convert_turn_to_dict(turn: str):
    # print(turn)
    turn = turn.strip()
    d = Counter()
    balls = turn.split(',')
    for ball in balls:
        if match_ := RE_NUM_TO_COLOUR.match(ball):
            d[match_['colour']] = int(match_['num'])
    # print(d)
    return d


def solution():
    s = 0
    for line in sys.stdin:
        game, results = line.split(":")
        _, game_num = game.split()
        game_num = int(game_num)
        # print(f"{game_num=}")
        turns = results.split(";")
        max_balls = {'red': 0 , 'blue': 0, 'green': 0}
        for turn in turns:
            turn_dict = convert_turn_to_dict(turn.strip())
            for colour, num in turn_dict.items():
                max_balls[colour] = max(max_balls[colour], num)
        s += math.prod(max_balls.values())
    return s


if __name__ == '__main__':
    print(f"Solution is: {solution()}")