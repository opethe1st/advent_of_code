"""
Just do it manually first.
"""
import re


instruction_regex = re.compile(pattern=r'(?P<type>toggle|turn on|turn off) (?P<top_left_x>\d+),(?P<top_left_y>\d+) through (?P<bottom_right_x>\d+),(?P<bottom_right_y>\d+)')


class Grid:
    def __init__(self):
        self._grid = [[0 for i in range(1000)] for j in range(1000)]

    def change_grid(self, instruction: str):
        match = instruction_regex.match(instruction)
        value = None
        match match.group('type'):
            case "toggle":
                value = 2
            case "turn on":
                value = 1
            case "turn off":
                value = (-1)

        self._change_brightness(
            value=value,
            top_left=(
                int(match.group('top_left_x')),
                int(match.group('top_left_y'))
            ),
            bottom_right=(
                int(match.group('bottom_right_x')),
                int(match.group('bottom_right_y'))
            )
        )

    def _change_brightness(self, value, top_left, bottom_right):
        for x in range(top_left[0], bottom_right[0]+1):
            for y in range(top_left[1], bottom_right[1]+1):
                self._grid[x][y] = max(self._grid[x][y]+value, 0)

    def total_brightness(self):
        return sum(sum(row) for row in self._grid)


if __name__ == '__main__':
    grid = Grid()
    # for instruction in ['turn on 0,0 through 0,0']:
    for instruction in open('input.txt'):
        grid.change_grid(instruction)

    print(grid.total_brightness())
