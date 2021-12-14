from collections import Counter
from itertools import pairwise
import math


def generate_pairs(polymer_template):
    return Counter("".join(chars) for chars in pairwise(polymer_template))


def do_pair_insertion(pairs, insertion_rules):
    new_pairs = Counter()
    for pair in pairs:
        if pair in insertion_rules:
            first, second = (
                pair[0] + insertion_rules[pair],
                insertion_rules[pair] + pair[1],
            )
            new_pairs[first] += pairs[pair]
            new_pairs[second] += pairs[pair]
    return new_pairs


def count_elements(pair_counter):
    char_counter = Counter()
    for pair, count in pair_counter.items():
        char_counter[pair[0]] += count
        char_counter[pair[1]] += count
    return char_counter


if __name__ == "__main__":
    file = open("input.txt", "r")
    polymer_template = file.readline().strip()
    file.readline()
    insertion_rules = dict(line.strip().split(" -> ") for line in file.readlines())
    file.close()

    pair_counter = generate_pairs(polymer_template=polymer_template)

    for _ in range(10):
        pair_counter = do_pair_insertion(pair_counter, insertion_rules)

    c = count_elements(pair_counter)
    highest_count = max(c.values())
    lowest_count = min(c.values())

    # using math.ceil here since the first and last letters appear just once
    # in the list of pairs, end up being odd in the count
    # divide by 2
    print(math.ceil(highest_count / 2) - math.ceil(lowest_count / 2))
