
def next_gen(laternfishes):
    ans = []
    new_fish = 0
    for fish in laternfishes:
        if fish == 0:
            new_fish += 1
            ans.append(6)
        else:
            ans.append(fish-1)
    return ans + [8]*new_fish

if __name__ == '__main__':
    laternfishes = list(map(int, input().split(',')))
    for day in range(80):
        laternfishes = next_gen(laternfishes)
        # print(laternfishes)
    print(len(laternfishes))
