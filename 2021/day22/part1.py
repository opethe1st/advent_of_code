"""
Advent of Code day 22, 2022
"""
import re
import dataclasses
import itertools


@dataclasses.dataclass
class Range:
    """represents a range, start - end"""

    start: int
    end: int

    def __post_init__(self):
        self.start = min(self.start, self.end)
        self.end = max(self.start, self.end)


@dataclasses.dataclass
class Cuboid:
    """represents a cuboid"""

    x_range: Range
    y_range: Range
    z_range: Range


def part1():
    """Solution to part 1"""
    cuboids = []
    for line in open("aoc_2021_22.in", encoding="utf-8"):
        if match := re.match(
            pattern=r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)",
            string=line,
        ):
            cuboids.append(
                (
                    match.group(1),
                    Cuboid(
                        x_range=Range(int(match.group(2)), int(match.group(3))),
                        y_range=Range(int(match.group(4)), int(match.group(5))),
                        z_range=Range(int(match.group(6)), int(match.group(7))),
                    ),
                )
            )
    lights = dict()
    for state, cuboid in cuboids:
        if not all(
            x in range(-50, 51)
            for x in {
                cuboid.x_range.start,
                cuboid.x_range.end,
                cuboid.y_range.start,
                cuboid.y_range.end,
                cuboid.z_range.start,
                cuboid.z_range.end,
            }
        ):
            continue
        for x in range(cuboid.x_range.start, cuboid.x_range.end + 1):
            for y in range(cuboid.y_range.start, cuboid.y_range.end + 1):
                for z in range(cuboid.z_range.start, cuboid.z_range.end + 1):
                    lights[(x, y, z)] = state

    print(sum(value == "on" for value in lights.values()))


def get_intervals(intervals, start, end):
    current = start
    while current != end:
        if current > end:
            raise Exception("this should not happen")
        yield current
        current = intervals[current]
    yield current


def part2():

    x_points = []
    y_points = []
    z_points = []

    instructions = []
    for line in open("aoc_2021_22.in", encoding="utf-8"):
        if match := re.match(
            pattern=r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)",
            string=line,
        ):
            x_points.append(int(match.group(2)))
            x_points.append(int(match.group(3)))
            y_points.append(int(match.group(4)))
            y_points.append(int(match.group(5)))
            z_points.append(int(match.group(6)))
            z_points.append(int(match.group(7)))
            instructions.append(
                (
                    match.group(1),
                    Cuboid(
                        x_range=Range(int(match.group(2)), int(match.group(3))),
                        y_range=Range(int(match.group(4)), int(match.group(5))),
                        z_range=Range(int(match.group(6)), int(match.group(7))),
                    ),
                )
            )

    x_intervals = {}
    y_intervals = {}
    z_intervals = {}
    x_points, y_points, z_points = (
        sorted(set(x_points)),
        sorted(set(y_points)),
        sorted(set(z_points)),
    )
    # print("x_points", len(x_points))
    # print("y_points", len(y_points))
    # print("z_points", len(z_points))
    for start, end in itertools.pairwise(x_points):
        x_intervals[start] = end

    for start, end in itertools.pairwise(y_points):
        y_intervals[start] = end

    for start, end in itertools.pairwise(z_points):
        z_intervals[start] = end

    # print(len(x_intervals), len(y_intervals), len(z_intervals))
    lights = {}

    i = 0
    for state, cuboid in reversed(instructions):
        if not all(
            x in range(-50, 51)
            for x in {
                cuboid.x_range.start,
                cuboid.x_range.end,
                cuboid.y_range.start,
                cuboid.y_range.end,
                cuboid.z_range.start,
                cuboid.z_range.end,
            }
        ):
            continue
        for x_start, x_end in itertools.pairwise(
            get_intervals(x_intervals, cuboid.x_range.start, cuboid.x_range.end)
        ):
            for y_start, y_end in itertools.pairwise(
                get_intervals(y_intervals, cuboid.y_range.start, cuboid.y_range.end)
            ):
                for z_start, z_end in itertools.pairwise(
                    get_intervals(z_intervals, cuboid.z_range.start, cuboid.z_range.end)
                ):
                    if not lights.get(
                        ((x_start, x_end), (y_start, y_end), (z_start, z_end))
                    ):
                        lights[
                            ((x_start, x_end), (y_start, y_end), (z_start, z_end))
                        ] = state
                        i += 1

    ans = 0
    for ((x_start, x_end), (y_start, y_end), (z_start, z_end)), state in lights.items():
        if state == "on":
            ans += (x_end - x_start + 1) * (y_end - y_start + 1) * (z_end - z_start + 1)
    print(ans)


if __name__ == "__main__":
    part1()
    part2()

