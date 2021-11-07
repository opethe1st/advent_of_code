
def neighbors(light_config: list[str], x: int, y: int):
    s = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx, dy) != (0, 0):
                if 0<= x+dx < len(light_config) and 0 <= y+dy < len(light_config[0]):
                    # print(x+dx, y+dy)
                    if light_config[x+dx][y+dy] == '#':
                        s += 1
    return s


def next_light_config(light_config: list[str])-> list[str]:
    lc = [['.' for _ in light_config[0]] for _ in light_config]
    for i in range(len(light_config)):
        for j in range(len(light_config[0])):
            if light_config[i][j] == '#':
                if neighbors(light_config, i, j) in {2, 3}:
                    lc[i][j] = '#'
                else:
                    lc[i][j] = '.'
            elif light_config[i][j] == '.':
                if neighbors(light_config, i, j) == 3:
                    lc[i][j] = '#'
                else:
                    lc[i][j] = '.'
            else:
                lc[i][j] = light_config[i][j]
    return lc


if __name__ == '__main__':
    light_config = list(row.strip() for row in open('input.txt'))
    for _ in range(100):
        light_config = next_light_config(light_config)
    print(sum(row.count('#') for row in light_config))
