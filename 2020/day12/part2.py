from dataclasses import dataclass
import math
import cmath


def next_state(state, instruction):
    current_direction, (current_x, current_y) = state
    direction, value = instruction
    if direction == 'N':
        return ((current_direction.real + (current_direction.imag+value)*1j), (current_x, current_y))
    elif direction == 'S':
        return ((current_direction.real + (current_direction.imag-value)*1j), (current_x, current_y))
    elif direction == 'W':
        return ((current_direction.real - value + (current_direction.imag)*1j), (current_x, current_y))
    elif direction == 'E':
        return ((current_direction.real + value + (current_direction.imag)*1j), (current_x, current_y))
    elif direction == 'L':
        return (current_direction*cmath.rect(1, math.pi/180*value), (current_x, current_y))
    elif direction == 'R':
        return (current_direction*cmath.rect(1, -math.pi/180*value), (current_x, current_y))
    elif direction == 'F':
        return (current_direction, (current_x+(value*current_direction.real), current_y+(value*current_direction.imag)))


if __name__ == "__main__":
    instructions = [(line[0], int(line[1:])) for line in (line.strip() for line in open('input.txt'))]
    state = ((10 + 1j), (0, 0))
    for instruction in instructions:
        state = next_state(state, instruction)
        # print(state)
    direction, (x, y) = state
    print(abs(x) + abs(y))
