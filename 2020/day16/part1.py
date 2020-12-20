import re
from functools import partial


FIELD_RE = re.compile(
    r"^(?P<first_start>\d+)-(?P<first_end>\d+) or (?P<second_start>\d+)-(?P<second_end>\d+)$"
)


def parse_field_to_validator(string):
    field_to_validator = {}
    for line in string.split("\n"):
        field, validator_line = line.split(":")
        match = FIELD_RE.match(validator_line.strip())
        first_start, first_end = int(match.group("first_start")), int(
            match.group("first_end")
        )
        second_start, second_end = int(match.group("second_start")), int(
            match.group("second_end")
        )

        def validator(x, first_start, first_end, second_start, second_end):
            return (x in range(first_start, first_end + 1)) or (
                x in range(second_start, second_end + 1)
            )

        field_to_validator[field.strip()] = partial(
            validator,
            first_start=first_start,
            first_end=first_end,
            second_start=second_start,
            second_end=second_end,
        )
    return field_to_validator


def parse_tickets(string):
    lines = string.split("\n")[1:]
    return [[int(num) for num in line.strip().split(",")] for line in lines]


if __name__ == "__main__":
    with open("test.txt") as file:
        sections = file.read().split("\n\n")
    field_to_validator = parse_field_to_validator(sections[0].strip())
    tickets = parse_tickets(sections[2].strip())

    sum_of_invalid = 0
    for ticket in tickets:
        for value in ticket:
            if not any(validator(value) for validator in field_to_validator.values()):
                sum_of_invalid += value

    print(sum_of_invalid)
