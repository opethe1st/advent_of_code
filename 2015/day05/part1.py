from itertools import zip_longest


def is_nice(s: str):
    has_three_vowels = len([c for c in s if c in 'aeiou']) >= 3
    has_two_letters_in_a_row = any(x == y for x, y in zip(s, s[1:]))
    has_forbidden_sequences = any(x+y in {'ab', 'cd', 'pq', 'xy'} for x, y in zip(s, s[1:]))
    return has_three_vowels and has_two_letters_in_a_row and not has_forbidden_sequences


if __name__ == '__main__':
    print(sum(is_nice(string) for string in open('input.txt')))
