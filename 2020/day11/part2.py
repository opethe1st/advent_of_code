from collections import defaultdict
from typing import Dict


def get_no_occupied(seats: Dict[tuple, str], position: tuple):
    x, y = position
    occupied = 0
    m, n = x, y
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx, dy) == (0, 0):
                continue
            xdx, ydy = x+dx, y+dy
            while True:
                if seats.get((xdx, ydy)) == '#':
                    occupied += 1
                    break
                elif seats.get((xdx, ydy)) == 'L':
                    break
                elif seats.get((xdx, ydy)) == '.':
                    xdx, ydy = xdx + dx, ydy + dy
                elif seats.get((xdx, ydy)) is None:
                    break
                else:
                    raise Exception(f'unknown seat type - {repr(seats.get((xdx, ydy)))}')
    return occupied


def simulate_one_step(seats: Dict[tuple, str], rows, cols):
    new_seats = {}
    for i in range(rows):
        for j in range(cols):
            occupied = get_no_occupied(seats, (i, j))
            if seats[(i, j)] == 'L' and occupied == 0:
                new_seats[(i, j)] = '#'
            elif seats[(i, j)] == '#' and occupied >= 5:
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
    while old_seats != seats:
        old_seats, seats = seats, simulate_one_step(seats, rows, cols)
    return number_of_occupied_seats(seats, rows, cols)


def print_seats(seats, rows, cols):
    ans = []
    for i in range(rows):
        ans.append(''.join(seats[(i, j)] for j in range(cols)))

    print('\n'.join(ans))


if __name__ == '__main__':
    seats = [line.strip() for line in open('input.txt')]
    seats_dict = {(i, j): seats[i][j] for i in range(len(seats)) for j in range(len(seats[0]))}
    ans = solve(seats_dict, len(seats), len(seats[0]))
    print(ans)
