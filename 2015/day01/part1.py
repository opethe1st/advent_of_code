if __name__ == '__main__':
    with open('input.txt') as file:
        instructions = file.read().strip()

    print(sum(map(lambda x: 1 if x == '(' else -1, instructions)))
