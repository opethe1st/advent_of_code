if __name__ == '__main__':
    with open('input.txt') as file:
        instructions = file.read().strip()

    floor = 0
    for i, bracket in enumerate(instructions, start=1):
        match bracket:
            case '(':
                floor += 1
            case ')':
                floor -= 1
            case _:
                raise Exception(f'unknown symbol: {bracket}')

        if floor == -1:
            print(i)
            break
