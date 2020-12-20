from typing import Dict

SIZE = 14


def simulate_one_step(seats: Dict[tuple, str]):
    new_seats = {}
    for i in range(-SIZE, SIZE):
        for j in range(-SIZE, SIZE):
            for k in range(-SIZE, SIZE):
                no_of_active_neighbors = number_of_active_neighbors(seats, (i, j, k))
                if seats.get((i, j, k), ".") == "#":
                    if no_of_active_neighbors in {2, 3}:
                        new_seats[(i, j, k)] = "#"
                    else:
                        new_seats[(i, j, k)] = "."
                elif seats.get((i, j, k), ".") == ".":
                    if no_of_active_neighbors == 3:
                        new_seats[(i, j, k)] = "#"
                    else:
                        new_seats[(i, j, k)] = "."
                else:
                    raise Exception("this should not happen")

    return new_seats


def number_of_occupied_seats(seats):
    count = 0
    for position in seats:
        count += int(seats.get(position, ".") == "#")
    return count


def number_of_active_neighbors(seats, point):
    x, y, z = point
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if (dx, dy, dz) != (0, 0, 0):
                    count += int(seats.get((x + dx, y + dy, z + dz), ".") == "#")
    return count


def solve(seats):
    for _ in range(6):
        seats = simulate_one_step(seats)
    return number_of_occupied_seats(seats)


if __name__ == "__main__":
    seats = [line.strip() for line in open("input.txt")]
    seats_dict = {
        (i, j, 0): seats[i][j]
        if (i in range(len(seats)) and j in range(len(seats[0])))
        else "."
        for i in range(-SIZE, SIZE)
        for j in range(-SIZE, SIZE)
    }

    ans = solve(seats_dict)
    print(ans)
