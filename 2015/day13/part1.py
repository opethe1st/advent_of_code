from collections import deque

def parse(line: str):
    match line.split():
        case [person1, "would", "lose", happiness_points, "happiness", "units", "by", "sitting", "next", "to", person2]:
            return person1, person2.rstrip("."), -int(happiness_points)
        case [person1, "would", "gain", happiness_points, "happiness", "units", "by", "sitting", "next", "to", person2]:
            return person1, person2.rstrip(". "), int(happiness_points)
        case _:
            raise Exception("unknown")


def optimal_seating_arrangment(graph, weights):
    return max(
        explore(
            graph,
            weights,
            deque([person]),
            person,
            0,
        )
        for person in graph
    )


def explore(graph, weights, visited, person, weight_so_far):
    if len(visited) == len(graph):
        return weight_so_far + weights[(person, visited[0])] + weights[(visited[0], person)]

    optimal = 0
    for neighbor in graph[person]:
        if neighbor not in visited:
            visited.append(neighbor)
            optimal = max(
                optimal,
                explore(
                    graph,
                    weights,
                    visited,
                    neighbor,
                    weight_so_far+weights[(person, neighbor)]+weights[(neighbor, person)]
                )
            )
            visited.pop()
    return optimal


if __name__ == '__main__':
    graph = dict()
    weights = dict()
    for line in open('input.txt'):
        person1, person2, happiness_points = parse(line)

        # print(person1, person2, happiness_points)
        weights[(person1, person2)] = happiness_points

        if person1 in graph:
            graph[person1].add(person2)
        else:
            graph[person1] = set([person2])

        if person2 in graph:
            graph[person2].add(person1)
        else:
            graph[person2] = set([person1])
    # print(graph)
    print(optimal_seating_arrangment(
        graph, weights
    ))
