from itertools import accumulate

invalid_number_from_step_1 = 1124361034

if __name__ == "__main__":
    numbers = [int(line.strip()) for line in open("input.txt")]
    prefix_sum = list(accumulate([0] + numbers))

    for i in range(len(numbers)):
        for j in range(i+2, len(numbers)):
            if (prefix_sum[j] - prefix_sum[i]) == invalid_number_from_step_1:
                print(max(numbers[i:j+1])+min(numbers[i:j+1]))
