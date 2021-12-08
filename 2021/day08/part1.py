

if __name__ == '__main__':
    no_of_times1478 = 0
    for line in open('input.txt'):
        _, output = line.split(' | ')
        nums = output.split()
        for num in nums:
            no_of_times1478 += (len(num) in {2, 3, 4, 7})
    print(no_of_times1478)
