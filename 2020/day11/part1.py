from collections import defaultdict
from typing import Dict


def get_neighbors(seats: Dict[tuple, str], position: tuple):
    x, y = position
    res = {'occupied': 0}
    count = 0
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if seats.get((x + dx, y + dy)) == '#':
            res['occupied'] += 1
    return res


def simulate_one_step(seats: Dict[tuple, str], rows, cols):
    new_seats = {}
    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbors(seats, (i, j))
            if seats[(i, j)] == 'L' and neighbors['occupied'] == 0:
                new_seats[(i, j)] = '#'
            elif seats[(i, j)] == '#' and neighbors['occupied'] >= 4:
                new_seats[(i, j)] = 'L'
            else:
                new_seats[(i, j)] = seats[(i, j)]

    return new_seats


def number_of_occupied_seats(seats, rows, cols):
    count = 0
    for i in range(rows):
        for j in range(cols):
            count += int(seats[(i, j)] == '#')
    return count

def solve(seats, rows, cols):
    old_seats, seats = seats, simulate_one_step(seats, rows, cols)
    count = 0
    while old_seats != seats:
        count +=1
        old_seats, seats = seats, simulate_one_step(seats, rows, cols)
        print(count)
    return number_of_occupied_seats(seats, rows, cols)

if __name__ == '__main__':
    seats = [line.strip() for line in open('input.txt')]
    seats_dict = {(i, j): seats[i][j] for i in range(len(seats)) for j in range(len(seats[0]))}
    ans = solve(seats_dict, len(seats), len(seats[0]))
    print(ans)
