from typing import Dict
import itertools


def simulate_one_step(seats: Dict[tuple, str], x, y, z, t):
    # not sure why this is called seats...lol
    new_seats = {}
    maxx, maxy, maxz, maxt = (0, 0, 0, 0)
    for seat in itertools.product(
        *[range(-x, x), range(-y, y), range(-z, z), range(-t, t)]
    ):
        no_of_active_neighbors = number_of_active_neighbors(seats, seat)
        if seats.get(seat, ".") == "#":
            if no_of_active_neighbors in {2, 3}:
                new_seats[seat] = "#"
                maxx, maxy, maxz, maxt = (
                    max(maxx, seat[0]),
                    max(maxy, seat[1]),
                    max(maxz, seat[2]),
                    max(maxt, seat[3]),
                )
            else:
                new_seats[seat] = "."
        elif seats.get(seat, ".") == ".":
            if no_of_active_neighbors == 3:
                new_seats[seat] = "#"
                maxx, maxy, maxz, maxt = (
                    max(maxx, seat[0]),
                    max(maxy, seat[1]),
                    max(maxz, seat[2]),
                    max(maxt, seat[3]),
                )
            else:
                new_seats[seat] = "."
        else:
            raise Exception("this should not happen")
    print((maxx, maxy, maxz, maxt))
    return new_seats, (maxx + 2, maxy + 2, maxz + 2, maxt + 2)


def number_of_occupied_seats(seats):
    count = 0
    for position in seats:
        count += int(seats.get(position, ".") == "#")
    return count


def number_of_active_neighbors(seats, point):
    x, y, z, t = point
    count = 0
    # 80 cycles here
    for (dx, dy, dz, dt) in itertools.product(range(-1, 2), repeat=4):
        if (dx, dy, dz, dt) != (0, 0, 0, 0):
            count += int(seats.get((x + dx, y + dy, z + dz, t + dt), ".") == "#")
    return count


def get_neighbors(point):
    x, y, z, t = point
    # 80 cycles here
    for (dx, dy, dz, dt) in itertools.product(range(-1, 2), repeat=4):
        if (dx, dy, dz, dt) != (0, 0, 0, 0):
            yield (x + dx, y + dy, z + dz, t + dt)


def solve(seats):
    x, y, z, t = 9, 9, 2, 2
    for _ in range(6):
        seats, (x, y, z, t) = simulate_one_step(seats, x=x, y=y, z=z, t=t)
    return number_of_occupied_seats(seats)


if __name__ == "__main__":
    seats = [line.strip() for line in open("input.txt")]
    seats_dict = {
        (i, j, 0, 0): seats[i][j]
        for i in range(len(seats))
        for j in range(len(seats[0]))
    }

    ans = solve(seats_dict)
    print(ans)
