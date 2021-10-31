"""
Just do it manually first.
"""
from dataclasses import dataclass
import re


toggle_regex = re.compile(pattern=r'toggle (?P<top_left_x>\d+),(?P<top_left_y>\d+) through (?P<bottom_right_x>\d+),(?P<bottom_right_y>\d+)')
turn_on_regex = re.compile(pattern=r'turn on (?P<top_left_x>\d+),(?P<top_left_y>\d+) through (?P<bottom_right_x>\d+),(?P<bottom_right_y>\d+)')
turn_off_regex = re.compile(pattern=r'turn off (?P<top_left_x>\d+),(?P<top_left_y>\d+) through (?P<bottom_right_x>\d+),(?P<bottom_right_y>\d+)')


class Grid:
    def __init__(self):
        self._grid = [[False for i in range(1000)] for j in range(1000)]

    def change_grid(self, instruction: str):
        if match := toggle_regex.match(instruction):
            self._toggle(
                top_left=(
                    int(match.group('top_left_x')),
                    int(match.group('top_left_y'))
                ),
                bottom_right=(
                    int(match.group('bottom_right_x')),
                    int(match.group('bottom_right_y'))
                )
            )
        elif match := turn_on_regex.match(instruction):
            self._change_status(
                status=True,
                top_left=(
                    int(match.group('top_left_x')),
                    int(match.group('top_left_y'))
                ),
                bottom_right=(
                    int(match.group('bottom_right_x')),
                    int(match.group('bottom_right_y'))
                )
            )
        elif match := turn_off_regex.match(instruction):
            self._change_status(
                status=False,
                top_left=(
                    int(match.group('top_left_x')),
                    int(match.group('top_left_y'))
                ),
                bottom_right=(
                    int(match.group('bottom_right_x')),
                    int(match.group('bottom_right_y'))
                )
            )

    def _toggle(self, top_left, bottom_right):
        for x in range(top_left[0], bottom_right[0]+1):
            for y in range(top_left[1], bottom_right[1]+1):
                self._grid[x][y] = not(self._grid[x][y])

    def _change_status(self, status, top_left, bottom_right):
        for x in range(top_left[0], bottom_right[0]+1):
            for y in range(top_left[1], bottom_right[1]+1):
                self._grid[x][y] = status

    def count_on(self):
        return sum(sum(row) for row in self._grid)
if __name__ == '__main__':
    grid = Grid()
    # for instruction in ['turn on 0,0 through 999,999']:
    for instruction in open('input.txt'):
        grid.change_grid(instruction)

    print(grid.count_on())
