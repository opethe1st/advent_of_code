from collections import Counter


def next_gen(laternfishes: dict):
    ans = Counter()
    for fish, count in laternfishes.items():
        if fish == 0:
            ans[8] += count
            ans[6] += count
        else:
            ans[fish-1] += count
    return ans

if __name__ == '__main__':
    laternfishes_list = list(map(int, input().split(',')))
    laternfishes = Counter(laternfishes_list)

    for day in range(256):
        laternfishes = next_gen(laternfishes)

    print(sum(laternfishes.values()))
