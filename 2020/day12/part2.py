import math
import cmath


def next_state(state, instruction):
    waypoint_position, ship_position = state
    direction, value = instruction
    if direction == "N":
        return (waypoint_position + value * 1j, ship_position)
    elif direction == "S":
        return (waypoint_position - value * 1j, ship_position)
    elif direction == "W":
        return (waypoint_position - value, ship_position)
    elif direction == "E":
        return (waypoint_position + value, ship_position)
    elif direction == "L":
        return (waypoint_position * cmath.rect(1, math.pi / 180 * value), ship_position)
    elif direction == "R":
        return (
            waypoint_position * cmath.rect(1, -math.pi / 180 * value),
            ship_position,
        )
    elif direction == "F":
        return (waypoint_position, ship_position + value * waypoint_position)


if __name__ == "__main__":
    instructions = [
        (line[0], int(line[1:]))
        for line in (line.strip() for line in open("input.txt"))
    ]
    state = ((10 + 1j), 0)
    for instruction in instructions:
        state = next_state(state, instruction)
        # print(state)
    waypoint_position, ship_position = state
    print(abs(ship_position.real) + abs(ship_position.imag))
