

if __name__ == '__main__':
    instruction_strings = [i for i in open('input.txt')]
    x, y = 0, 0
    for instruction_string in instruction_strings:
        match instruction_string.split():
            case ["forward", distance]:
                x += int(distance)
            case ["down", distance]:
                y += int(distance)
            case ["up", distance]:
                y -= int(distance)
    print(x*y)
