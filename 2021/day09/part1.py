def solution(heightmap):
    low_points = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            neighbors = []
            if i > 0:
                neighbors.append(heightmap[i - 1][j])
            if j > 0:
                neighbors.append(heightmap[i][j - 1])
            if i < len(heightmap) - 1:
                neighbors.append(heightmap[i + 1][j])
            if j < len(heightmap[0]) - 1:
                neighbors.append(heightmap[i][j + 1])
            if heightmap[i][j] < min(neighbors):
                low_points.append(heightmap[i][j])
    return sum(point + 1 for point in low_points)


if __name__ == "__main__":
    heightmap = [[int(height) for height in row.strip()] for row in open("input.txt")]
    print(solution(heightmap))
