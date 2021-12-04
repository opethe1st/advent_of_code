
def most_common_bit(binary_nums, position):
    majority_bit = '1' if sum(int(num[position]) for num in binary_nums) >= len(binary_nums)/2 else '0'
    return list(filter(lambda x: x[position] == majority_bit, binary_nums))

def least_common_bit(binary_nums, position):
    majority_bit = '1' if sum(int(num[position]) for num in binary_nums) < len(binary_nums)/2 else '0'
    return list(filter(lambda x: x[position] == majority_bit, binary_nums))


if __name__ == '__main__':
    binary_numbers = [x.strip() for x in open('input.txt')]
    binary_num_size = len(binary_numbers[0])
    oxygen_gen_ratings = binary_numbers
    for position in range(binary_num_size):
        oxygen_gen_ratings = most_common_bit(oxygen_gen_ratings, position)
        if len(oxygen_gen_ratings) == 1:
            break

    co2_scrubber_ratings = binary_numbers
    for position in range(binary_num_size):
        co2_scrubber_ratings = least_common_bit(co2_scrubber_ratings, position)
        if len(co2_scrubber_ratings) == 1:
            break

    print(
        int(oxygen_gen_ratings[0], base=2) * int(co2_scrubber_ratings[0], base=2)
    )
