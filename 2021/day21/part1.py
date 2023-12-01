"""
Player 1 starting position: 1
Player 2 starting position: 5
"""
import itertools
from collections import defaultdict


def solution(player_1_start_position, player_2_start_position):
    '''solution to part 1'''
    starting_positions = [player_1_start_position, player_2_start_position]
    scores = [0, 0]

    dice = itertools.cycle(range(1, 101))
    no_of_rolls = 0
    current_player = False
    while True:
        distance = next(dice) + next(dice) + next(dice)
        no_of_rolls += 3

        starting_positions[current_player] = (
            starting_positions[current_player] + distance - 1
        ) % 10 + 1
        scores[current_player] += starting_positions[current_player]

        if scores[current_player] >= 1000:
            # print(scores[not current_player], no_of_rolls)
            return scores[not current_player] * no_of_rolls
        current_player = not current_player


def part_2_solution(starting_positions):
    """solution to part 2"""

    # possible dice sums for 3 rolls
    possible_distances = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

    position_score_to_universes = {((starting_positions[0], 0), (starting_positions[1], 0)): 1}
    universe_wins = [0, 0]

    count = 0
    for current_player in itertools.cycle([False, True]):
        # time.sleep(2)
        new_position_score_to_universes = defaultdict(int)
        if not position_score_to_universes:
            break
        for (
            (player1_position, player1_score),
            (player2_position, player2_score),
        ), universes in position_score_to_universes.items():
            for distance, no_universes in possible_distances.items():
                if not current_player:
                    new_position = (player1_position + distance - 1) % 10 + 1
                    new_score = player1_score + new_position
                    if new_score >= 21:
                        universe_wins[current_player] += universes * no_universes
                        continue
                    new_position_score_to_universes[
                        ((new_position, new_score), (player2_position, player2_score))
                    ] += (universes * no_universes)
                else:
                    new_position = (player2_position + distance - 1) % 10 + 1
                    new_score = player2_score + new_position
                    if new_score >= 21:
                        universe_wins[current_player] += universes * no_universes
                        continue
                    new_position_score_to_universes[
                        ((player1_position, player1_score), (new_position, new_score))
                    ] += (universes * no_universes)

        position_score_to_universes = new_position_score_to_universes
        # print(position_score_to_universes)
        # print(count)
        count += 1
        # print()
    # print(universe_wins)
    return max(universe_wins)


if __name__ == "__main__":
    print(solution(1, 5))
    print(part_2_solution([4, 8]))
    print(part_2_solution([1, 5]))
