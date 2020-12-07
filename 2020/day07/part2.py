import re
from collections import defaultdict


LINE_REGEX = re.compile(r'^(?P<container_bag>[a-z]+ [a-z]+) bags contain (?P<bag_count>[0-9]+) (?P<bag>[a-z]+ [a-z]+) bags?')
BAG_REGEX = re.compile(r', (?P<bag_count>[0-9]+) (?P<bag>[a-z]+ [a-z]+) bags?')


def parse_graph():
    lines = [line.strip() for line in open('input.txt')]
    graph = defaultdict(list)
    for line in lines:
        match = LINE_REGEX.match(line)
        if match:
            container = match.group('container_bag')
            bag = match.group('bag')
            graph[container].extend([bag]*int(match.group('bag_count')))
            for match in BAG_REGEX.finditer(string=line, pos=match.span()[1]):
                bag = match.group('bag')
                graph[container].extend([bag]*int(match.group('bag_count')))
    return graph


def count_bags(graph):
    stack = ['shiny gold']
    count = 0
    while stack:
        bag = stack.pop()
        count += 1
        for container_bag in graph[bag]:
            stack.append(container_bag)
    return count - 1

if __name__ == '__main__':
    graph = parse_graph()
    print(count_bags(graph=graph))
