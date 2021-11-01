from collections import defaultdict


def build_graph():
    graph = dict()
    weights = defaultdict(int)
    for line in open('input.txt'):
        match line.split():
            case [from_city, _, to_city, _, distance]:
                if from_city in graph:
                    graph[from_city].append(to_city)
                else:
                    graph[from_city] = [to_city]
                if to_city in graph:
                    graph[to_city].append(from_city)
                else:
                    graph[to_city] = [from_city]
                weights[(from_city, to_city)] = int(distance)
                weights[(to_city, from_city)] = int(distance)

    return graph, weights


def shortest_distance_to_visit_all_cities(graph, weights):
    return min(
        shortest_distance_to_remaining_cities(
            graph,
            weights,
            city,
            set([city]),
            0,
        ) for city in graph.keys()
    )

def shortest_distance_to_remaining_cities(graph, weights, city, visited, shortest_distance_so_far):
    # print(city, visited)
    if len(visited) == len(graph):
        # print(shortest_distance_so_far)
        # print()
        return shortest_distance_so_far

    shortest = float('inf')
    for neighbor in graph.get(city, []):
        if neighbor not in visited:
            visited.add(neighbor)
            shortest = min(
                shortest_distance_to_remaining_cities(
                    graph,
                    weights,
                    neighbor,
                    visited,
                    shortest_distance_so_far+weights[(city, neighbor)]
                ),
                shortest
            )
            visited.remove(neighbor)
    return shortest


if __name__ == '__main__':
    graph, weights = build_graph()
    print(shortest_distance_to_visit_all_cities(graph, weights))
