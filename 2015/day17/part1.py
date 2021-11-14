def get_number_of_combinations(capacity, containers):
    if capacity < 0:
        return 0
    if capacity == 0:
        return 1
    if not containers:
        return 0

    s = 0
    for i in range(len(containers)):
        container = containers[i]
        s += get_number_of_combinations(capacity-container, containers[i+1:])
    return s


if __name__ == '__main__':
    containers =list(map(int, open('input.txt')))
    print(get_number_of_combinations(150, containers))
