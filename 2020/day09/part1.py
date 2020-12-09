
if __name__ == "__main__":
    numbers = [int(line.strip()) for line in open("input.txt")]
    for index in range(25, len(numbers)):
        sums_of_previous = set(numbers[index - i] + numbers[index - j] for i in range(1, 26) for j in range(i))
        if numbers[index] not in sums_of_previous:
            print(index, numbers[index])
            break
