'''
This solution is a standard solution you can find on Leetcode for 3 sum.
'''

from collections import Counter

nums = sorted([int(num) for num in open('input.txt')])

for start in range(len(nums)):
    left, right = start + 1, len(nums) - 1
    while left < right:
        s = nums[start] + nums[left] + nums[right]
        if s == 2020:
            print(nums[start] * nums[left] * nums[right])
            break
        elif s < 2020:
            left += 1
        else:
            right -= 1
