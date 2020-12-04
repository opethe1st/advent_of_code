from collections import Counter


# couldn't be bothered to even create a function.. haha
nums = Counter([int(num) for num in open('input.txt')])
for num in nums:
    if num == 1010:
        if nums[num] > 1:
            print(num * num)
            break
    elif (2020 - num) in nums:
        print(num * (2020 - num))
        break
