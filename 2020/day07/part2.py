import re
from collections import defaultdict


LINE = re.compile(r'^([a-z]+ [a-z]+) bags contain ([0-9])+ ([a-z]+ [a-z]+) bags?')
BAG_REGEX = re.compile(r'^, ([0-9]+) ([a-z]+ [a-z]+) bags?')
NO_OTHER_BAG_RE = re.compile(r'^([a-z]* [a-z]*) bags contain no other bags.$')


def parse_graph():
    lines = [line.strip() for line in open('input.txt')]
    graph = defaultdict(list)
    for line in lines:
        match = NO_OTHER_BAG_RE.match(line)
        if match:
            continue
        match = LINE.match(line)
        container = match.group(1)
        n = int(match.group(2))
        bag = match.group(3)
        graph[container].extend([bag]*n)
        if match:
            _, end = match.span()
            line = line[end:]
            while line and line != '.':
                match = BAG_REGEX.match(line)
                n = int(match.group(1))
                bag = match.group(2)
                # print(bag)
                graph[container].extend([bag]*n)

                _, end = match.span()
                line = line[end:]
    # print(graph)
    return graph


def parse_bag(line):
    bag, rest_of_line = parse_words(line=line, n=2)


def number_of_unique_ancestors(graph):
    stack = ['shiny gold']
    count = 0
    while stack:
        bag = stack.pop()
        count += 1
        for container_bag in graph.get(bag, []):
            stack.append(container_bag)
    return count - 1

if __name__ == '__main__':
    graph = parse_graph()
    print(number_of_unique_ancestors(graph=graph))
