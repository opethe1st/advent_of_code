import sys
import string


def get_first_last_digit(line):
    # what happens if there is only one digit in line? Ignoring that case for now
    first = next(ch for ch in line if ch in string.digits)
    last = next(ch for ch in reversed(line) if ch in string.digits)
    return int(first+last)

def solution_part_1():
    s = 0
    for line in sys.stdin:
        s += get_first_last_digit(line)
    return s

if __name__ == '__main__':
    print(f"part 1: {solution_part_1()}")

