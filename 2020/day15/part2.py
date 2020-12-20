from collections import defaultdict


if __name__ == "__main__":
    starting_numbers = [0, 14, 1, 3, 7, 9]
    numbers = starting_numbers[:]
    most_recently_spoken = defaultdict(list)
    for turn, number in enumerate(starting_numbers, start=1):
        most_recently_spoken[number].append(turn)

    for turn in range(len(starting_numbers) + 1, 30000000 + 1):
        last_spoken = numbers[-1]
        if len(most_recently_spoken[last_spoken]) <= 1:
            num = 0
        else:
            num = (
                most_recently_spoken[last_spoken][-1]
                - most_recently_spoken[last_spoken][-2]
            )
        numbers.append(num)
        most_recently_spoken[num].append(turn)

    print(numbers[30000000 - 1])
