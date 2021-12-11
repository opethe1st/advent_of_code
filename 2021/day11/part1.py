from itertools import product


def get_neighbors(point, row_size, col_size):
    x, y = point
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx or dy) and (0 <= (x + dx) < row_size) and (0 <= (y + dy) < col_size):
                yield x + dx, y + dy


def increase_all_energy_levels(grid):
    return [[item + 1 for item in row] for row in grid]


def cascade_flashing(grid):
    changed = True
    flashed = set()
    while changed:
        changed = False
        for x, y in product(range(len(grid)), range(len(grid[0]))):
            if grid[x][y] > 9 and (x, y) not in flashed:
                flashed.add((x, y))
                changed = True
                for i, j in get_neighbors((x, y), len(grid), len(grid[0])):
                    grid[i][j] += 1
    for x, y in flashed:
        grid[x][y] = 0
    return grid, len(flashed)


def print_grid(grid):
    print("\n".join("".join(str(item) for item in row) for row in grid))


if __name__ == "__main__":
    grid = [list(map(int, line.strip())) for line in open("input.txt")]
    print(grid)
    s = 0
    for _ in range(100):
        grid = increase_all_energy_levels(grid)
        grid, no_of_flashes = cascade_flashing(grid)
        s += no_of_flashes
    print(s)
