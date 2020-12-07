from functools import reduce

if __name__ == '__main__':
    with open('input.txt') as file:
        inp = file.read()
    groups = [line.strip().split('\n') for line in inp.split('\n\n')]
    print(
        sum(
            len(
                reduce(lambda x, y: set(x) & set(y), group)
            ) for group in groups
        )
    )
