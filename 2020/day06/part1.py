


if __name__ == '__main__':
    with open('input.txt') as file:
        inp = file.read()
    groups = [line.strip().split('\n') for line in inp.split('\n\n')]
    print(
        sum(len(set("".join(group))) for group in groups)
    )
