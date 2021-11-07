
aunty_sue_properties ={
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
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
    return all(properties[prop] == aunty_sue_properties[prop] for prop in properties)


if __name__ == '__main__':
    for line in open('input.txt'):
        id, properties = parse(line)
        if is_correct_aunty_sue(properties):
            print(id)
