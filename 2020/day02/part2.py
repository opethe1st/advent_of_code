from collections import Counter
import re
from typing import List


class Policy:
    # could use named groups here
    POLICY_PATTERN = re.compile(r'(\d+)\-(\d+) ([a-z])')
    def __init__(self, letter: str, positions: List[int]):
        self.letter = letter
        self.positions = positions

    @classmethod
    def from_string(cls, policy: str):
        match = cls.POLICY_PATTERN.match(policy.strip())
        return cls(
            letter=match.group(3),
            positions=[int(match.group(1)), int(match.group(2))]
        )


def is_valid(policy: Policy, password: str) -> bool:
    letter_freq = Counter([password[position] for position in policy.positions])
    return letter_freq[policy.letter] == 1


if __name__ == '__main__':
    count = 0
    for line in open('input.txt'):
        policy, password = line.split(':')
        count += int(is_valid(policy=Policy.from_string(policy=policy), password=password))
    print(count)
