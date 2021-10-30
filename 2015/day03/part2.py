from dataclasses import dataclass
from itertools import islice


@dataclass(eq=True, unsafe_hash=True)
class Position:
    x: int
    y: int


def next_position(position: Position, direction: str) -> Position:
    match direction:
        case '^':
            return Position(position.x, position.y+1)
        case '>':
            return Position(position.x+1, position.y)
        case '<':
            return Position(position.x-1, position.y)
        case 'v':
            return Position(position.x, position.y-1)
        case _:
            raise Exception('unexpected direction', direction)


if __name__ == '__main__':
    with open('input.txt') as file:
        directions = file.read().strip()
    start_position = Position(0, 0)
    unique_positions = set([start_position])

    position = start_position
    for direction in islice(directions, 0, None, 2):
        position = next_position(position, direction)
        unique_positions.add(position)

    position = start_position
    for direction in islice(directions, 1, None, 2):
        position = next_position(position, direction)
        unique_positions.add(position)
    print(len(unique_positions))
