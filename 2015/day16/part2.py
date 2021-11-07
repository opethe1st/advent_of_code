aunty_sue_properties = {
    'cats': 7 .__lt__,
    'trees': 3 .__lt__,
    'pomeranians': 3 .__gt__,
    'goldfish': 5 .__gt__,
    'children': 3 .__eq__,
    'samoyeds': 2 .__eq__,
    'akitas': 0 .__eq__,
    'vizslas': 0 .__eq__,
    'cars': 2 .__eq__,
    'perfumes': 1 .__eq__,
}

def parse(line):
    match line.split():
        case [_, id, prop1, val1, prop2, val2, prop3, val3]:
            return id.rstrip(":"), {
                prop1.rstrip(":"): int(val1.rstrip(',')),
                prop2.rstrip(":"): int(val2.rstrip(',')),
                prop3.rstrip(":"): int(val3.rstrip(',')),
            }
        case _:
            raise Exception('this should not happen')


def is_correct_aunty_sue(properties: dict) -> bool:
    return all(aunty_sue_properties[prop](properties[prop]) for prop in properties)


if __name__ == '__main__':
    for line in open('input.txt'):
        id, properties = parse(line)
        if is_correct_aunty_sue(properties):
            print(id)
