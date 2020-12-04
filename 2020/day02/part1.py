from collections import Counter
import re


class Policy:
    # could have used named groups here
    POLICY_PATTERN = re.compile(r'(\d+)\-(\d+) ([a-z])')
    def __init__(self, letter: str, minimum: int, maximum: int):
        self.letter = letter
        self.minimum = minimum
        self.maximum = maximum

    @classmethod
    def from_string(cls, policy: str):
        match = cls.POLICY_PATTERN.match(policy.strip())
        return cls(letter=match.group(3), minimum=int(match.group(1)), maximum=int(match.group(2)))

# classic OOP would have this be a method on Policy. I think a better model of the problem is to write it such that
# validation is an external thing, a policy can not validate itself. It is not sentient :).
def is_valid(policy: Policy, password: str) -> bool:
    letter_freq = Counter(password)
    return policy.minimum <= letter_freq[policy.letter] <= policy.maximum


if __name__ == '__main__':
    count = 0
    for line in open('input.txt'):
        policy, password = line.split(':')
        count += int(is_valid(policy=Policy.from_string(policy=policy), password=password))
    print(count)
