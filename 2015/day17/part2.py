"""
--- Part Two ---
While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.
"""
from collections import defaultdict


def get_minimum_no_of_containers(capacity, containers, containers_so_far:int, no_of_containers_to_count: dict):
    if capacity < 0:
        return float('inf')
    if capacity == 0:
        no_of_containers_to_count[containers_so_far] += 1
        return containers_so_far
    if not containers:
        return float('inf')

    m = float('inf')
    for i in range(len(containers)):
        container = containers[i]
        m = min(
            get_minimum_no_of_containers(
                capacity-container,
                containers[i+1:],
                containers_so_far+1,
                no_of_containers_to_count
            ),
            m
        )
    return m


if __name__ == '__main__':
    containers = list(map(int, open('input.txt')))
    no_of_containers_to_count = defaultdict(int)
    minimum_no_containers = get_minimum_no_of_containers(
        150,
        containers,
        0,
        no_of_containers_to_count
    )
    print(no_of_containers_to_count[minimum_no_containers])
