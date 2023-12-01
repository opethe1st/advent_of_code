import sys
import string

STRING_TO_NUM = {
    "0": '0',
    "1": '1',
    "2": '2',
    "3": '3',
    "4": '4',
    "5": '5',
    "6": '6',
    "7": '7',
    "8": '8',
    "9": '9',
    "0": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}

def get_first_last_digit_2(line):
    # what happens if there is only one digit in line? Ignoring that case for now
    first, last = None, None
    for i in range(len(line)):  # pylint: disable=C0200
        if not first:
            for s in STRING_TO_NUM:
                if line[i:].startswith(s):
                    first = STRING_TO_NUM[s]
                    last = STRING_TO_NUM[s]
        else:
            if line[i] in string.digits:
                last = line[i]
            else:
                for s in STRING_TO_NUM:
                    if line[i:].startswith(s):
                        last = STRING_TO_NUM[s]
    return int(first+last)

def solution_part_2():
    s = 0
    for line in sys.stdin:
        s += get_first_last_digit_2(line)
    return s



if __name__ == '__main__':
    print(f"part 2: {solution_part_2()}")
