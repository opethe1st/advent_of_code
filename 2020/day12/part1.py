from dataclasses import dataclass
import math


def next_state(state, instruction):
    current_direction, (current_x, current_y) = state
    direction, value = instruction
    if direction == 'N':
        return (current_direction, (current_x, current_y + value))
    elif direction == 'S':
        return (current_direction, (current_x, current_y - value))
    elif direction == 'W':
        return (current_direction, (current_x - value, current_y))
    elif direction == 'E':
        return (current_direction, (current_x + value, current_y))
    elif direction == 'L':
        return (current_direction+value, (current_x, current_y))
    elif direction == 'R':
        return (current_direction-value, (current_x, current_y))
    elif direction == 'F':
        return (current_direction, (current_x+(value*math.cos(math.pi/180*current_direction)), current_y+(value*math.sin(math.pi/180*current_direction))))


if __name__ == "__main__":
    instructions = [(line[0], int(line[1:])) for line in (line.strip() for line in open('input.txt'))]
    state = (0, (0, 0))
    for instruction in instructions:
        state = next_state(state, instruction)
    direction, (x, y) = state
    print(abs(x) + abs(y))
