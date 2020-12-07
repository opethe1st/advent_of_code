import re
from collections import defaultdict


LINE_REGEX = re.compile(r'^(?P<container_bag>[a-z]+ [a-z]+) bags contain [0-9]+ (?P<bag>[a-z]+ [a-z]+) bags?')
BAG_REGEX = re.compile(r', [0-9]+ (?P<bag>[a-z]+ [a-z]+) bags?')


def parse_graph():
    lines = [line.strip() for line in open('input.txt')]
    graph = defaultdict(list)
    for line in lines:
        match = LINE_REGEX.match(line)
        if match:
            container = match.group('container_bag')
            bag = match.group('bag')
            graph[bag].append(container)
            for match in BAG_REGEX.finditer(string=line, pos=match.span()[1]):
                bag = match.group('bag')
                graph[bag].append(container)
    return graph


def number_of_unique_containers(graph):
    stack = ['shiny gold']
    unique_containers = set()
    while stack:
        bag = stack.pop()
        unique_containers.add(bag)
        for container_bag in graph[bag]:
            stack.append(container_bag)
    return len(unique_containers) - 1  # subtracting one to exclude the shiny gold bag

if __name__ == '__main__':
    graph = parse_graph()
    print(number_of_unique_containers(graph=graph))
