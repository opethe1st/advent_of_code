if __name__ == "__main__":
    binary_numbers = [x for x in open("input.txt")]
    binary_num_size = len(binary_numbers[0])

    one_counts = [0 for _ in range(binary_num_size)]
    for num in binary_numbers:
        for i in range(binary_num_size):
            one_counts[i] += int(num[i])

    gamma_rate = "".join(
        [str(int(count > len(binary_numbers) // 2)) for count in one_counts]
    )
    epilson_rate = "".join(
        [str(int(count <= len(binary_numbers) // 2)) for count in one_counts]
    )
    print(int(gamma_rate, base=2) * int(epilson_rate, base=2))
