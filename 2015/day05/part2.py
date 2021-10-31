from itertools import pairwise


def triplewise(iterable):
    "Return overlapping triplets from an iterable"
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


def is_nice(s: str):
    has_one_letter_which_repeats_with_exactly_one_letter = any(
        s[0] == s[-1] for s in triplewise(s)
    )
    has_pair_of_letters_not_overlapping = False
    pair_to_last_location = dict()
    for i, _ in enumerate(s):
        pair = s[i:i+2]
        if pair in pair_to_last_location and pair_to_last_location[pair] < (i - 1):
            has_pair_of_letters_not_overlapping = True
            break
        pair_to_last_location[s[i:i+2]] = i
    return has_pair_of_letters_not_overlapping and has_one_letter_which_repeats_with_exactly_one_letter


if __name__ == '__main__':
    # print(sum(is_nice(string) for string in ['ieodomkazucvgmuy']))
    print(sum(is_nice(string) for string in open('input.txt')))
