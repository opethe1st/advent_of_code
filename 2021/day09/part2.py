from collections import defaultdict


def get_neighbors(point, row_size, col_size):
    neighbors = []
    i, j = point
    if i > 0:
        neighbors.append((i - 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if i < (row_size - 1):
        neighbors.append((i + 1, j))
    if j < (col_size - 1):
        neighbors.append((i, j + 1))
    return neighbors


def get_low_points(heightmap):
    low_points = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if heightmap[i][j] < min(
                heightmap[x][y]
                for x, y in get_neighbors((i, j), len(heightmap), len(heightmap[0]))
            ):
                low_points.append((i, j))
    return low_points


def build_graph(heightmap):
    graph = defaultdict(set)

    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if heightmap[i][j] == 9:
                continue

            for x, y in get_neighbors((i, j), len(heightmap), len(heightmap[0])):
                if heightmap[i][j] < heightmap[x][y]:
                    if heightmap[x][y] != 9:
                        graph[(i, j)].add((x, y))
    return graph


def get_components(graph, low_points):
    visited = set()
    components = []
    for i, j in low_points:
        if (i, j) not in visited:
            component= explore(graph, (i, j), visited)
            components.append(component)
    return components


def explore(graph, start, visited):
    stack = [start]
    component = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        component.append(node)
        for next_node in graph[node]:
            if next_node not in visited:
                stack.append(next_node)

    return component


def solution(heightmap):
    low_points = get_low_points(heightmap)
    graph = build_graph(heightmap)
    components = get_components(graph, low_points)
    component_sizes = sorted([len(component) for component in components])
    return component_sizes[-3] * component_sizes[-2] * component_sizes[-1]


if __name__ == "__main__":
    heightmap = [[int(height) for height in row.strip()] for row in open("input.txt")]
    print(solution(heightmap))
