import json


def sum_integers(obj):
    match obj:
        case list() as obj:
            return sum(sum_integers(x) for x in obj)
        case dict() as obj:
            if "red" in obj.values():
                return 0
            return sum(sum_integers(x) for x in obj.keys()) + sum(sum_integers(x) for x in obj.values())
        case int() as obj:
            return obj
        case _:
            return 0


if __name__ == '__main__':
    with open('input.txt') as file:
        obj = json.loads(file.read())

    print(sum_integers(obj))
