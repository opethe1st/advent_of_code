from collections import defaultdict


def solve(sorted_joltages):
    no_of_ways = defaultdict(int)
    no_of_ways[0] = 1
    for jolt in sorted_joltages:
        no_of_ways[jolt] += (no_of_ways[jolt-1] + no_of_ways[jolt-2] + no_of_ways[jolt-3])
    return no_of_ways[sorted_joltages[-1]]

if __name__ == '__main__':
    joltages = [int(line) for line in open('input.txt')]
    sorted_joltages = sorted(joltages)
    sorted_joltages = [0] + sorted_joltages + [sorted_joltages[-1] + 3]

    ans = solve(sorted_joltages)
    print(ans)
