from os import name
import re
from collections import defaultdict
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
Line = namedtuple("Line", ["start", "end"])


def is_horizontal(line: Line):
    return line.start.y == line.end.y


def is_vertical(line: Line):
    return line.start.x == line.end.x


def points_on_line(line):
    point1, point2 = line
    dx = (point2.x - point1.x) // max(abs((point2.x - point1.x)), 1)
    dy = (point2.y - point1.y) // max(abs((point2.y - point1.y)), 1)
    point = point1
    while point != point2:
        yield point
        point = Point(point.x + dx, point.y + dy)
    yield point2


LINE_RE = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
if __name__ == "__main__":
    lines = []

    for line in open("input.txt"):
        match = LINE_RE.match(line)
        x1, y1 = int(match.group(1)), int(match.group(2))
        x2, y2 = int(match.group(3)), int(match.group(4))
        lines.append(Line(Point(x1, y1), Point(x2, y2)))

    lines_overlap = defaultdict(int)
    for line in lines:
        if is_horizontal(line) or is_vertical(line):
            for point in points_on_line(line):
                lines_overlap[point] += 1

    print(sum(count > 1 for count in lines_overlap.values()))
