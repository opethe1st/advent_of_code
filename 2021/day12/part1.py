from collections import defaultdict


def get_all_distinct_paths(graph: dict, start: str, visited: set, path_so_far):
    if start == "end":
        return set([path_so_far])

    distinct_paths = set()
    for neighbor in graph[start]:
        if neighbor == neighbor.lower() and neighbor not in visited:
            visited.add(neighbor)
            paths = get_all_distinct_paths(
                graph, neighbor, visited, path_so_far + (neighbor,)
            )
            visited.remove(neighbor)
            distinct_paths |= paths
        if neighbor != neighbor.lower():
            paths = get_all_distinct_paths(
                graph, neighbor, visited, path_so_far + (neighbor,)
            )
            distinct_paths |= paths

    return distinct_paths


if __name__ == "__main__":
    graph = defaultdict(set)

    for line in open("input.txt"):
        line = line.strip()
        node1, node2 = line.split("-")
        graph[node1].add(node2)
        graph[node2].add(node1)

    visited = set(["start"])
    path_so_far = ("start",)
    start = "start"
    paths = get_all_distinct_paths(
        graph, start=start, visited=visited, path_so_far=path_so_far
    )
    print(len(paths))
