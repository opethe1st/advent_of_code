import math
import cmath


def next_state(state, instruction):
    current_direction, position = state
    direction, value = instruction
    if direction == "N":
        return (current_direction, position + value * 1j)
    elif direction == "S":
        return (current_direction, position - value * 1j)
    elif direction == "W":
        return (current_direction, position - value)
    elif direction == "E":
        return (current_direction, position + value)
    elif direction == "L":
        return (current_direction + value, position)
    elif direction == "R":
        return (current_direction - value, position)
    elif direction == "F":
        return (
            current_direction,
            position + value * cmath.rect(1, current_direction * math.pi / 180),
        )


if __name__ == "__main__":
    instructions = [
        (line[0], int(line[1:]))
        for line in (line.strip() for line in open("input.txt"))
    ]
    state = (0, 0)
    for instruction in instructions:
        state = next_state(state, instruction)
    direction, position = state
    print(abs(position.real) + abs(position.imag))
