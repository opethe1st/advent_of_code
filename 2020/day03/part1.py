

def tree_in_slope(area, slope):
    count = 0
    dx, dy = slope
    x, y = 0, 0
    # what happens if the dy is 0?
    while y < len(area):
        count += int(area[y][x] == '#')  # yes, I know this isnt necessary in python
        x, y = (x + dx)%len(area[0]), y + dy
    return count


if __name__ == '__main__':
    # Basic test
    # print(tree_in_slope(area=['XX', 'XX', 'X.'], slope=(1, 2)))
    area = [row.strip() for row in open('input.txt')]
    print(tree_in_slope(area=area, slope=(3, 1)))
