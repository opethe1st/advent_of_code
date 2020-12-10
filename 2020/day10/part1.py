

if __name__ == '__main__':
    joltages = [int(line) for line in open('input.txt')]
    sorted_joltages = sorted(joltages)
    # print(sorted_joltages[:10])

    number_of_1_differences = 0
    number_of_3_differences = 0
    for jolt, next_jolt in zip([0] + sorted_joltages, sorted_joltages + [sorted_joltages[-1] + 3]):
        # print(jolt, next_jolt)
        if (next_jolt - jolt) == 1:
            number_of_1_differences += 1
        if (next_jolt - jolt) == 3:
            number_of_3_differences += 1
    print(number_of_1_differences * number_of_3_differences)
