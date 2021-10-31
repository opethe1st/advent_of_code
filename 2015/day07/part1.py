from dataclasses import dataclass
from typing import Any
import re


@dataclass
class And:
    x: Any
    y: Any


@dataclass
class Or:
    x: Any
    y: Any


@dataclass
class Lshift:
    x: Any
    y: int


@dataclass
class Rshift:
    x: Any
    y: int


@dataclass
class Not:
    x: Any


@dataclass
class Same:
    x: Any


def parse_wire(circuit, wire):
    match wire.split():
        case [num, _, variable]:
            circuit[variable] = Same(num)
        case [x, "AND", y, _, variable]:
            circuit[variable] = And(x, y)
        case [x, "OR", y, _, variable]:
            circuit[variable] = Or(x, y)
        case [x, "LSHIFT", y, _, variable]:
            # need to fix, x can be an integer
            circuit[variable] = Lshift(x, (y))
        case [x, "RSHIFT", y, _, variable]:
            circuit[variable] = Rshift(x, (y))
        case ["NOT", x, _, variable]:
            circuit[variable] = Not(x)



NUMBER = re.compile(r'\d+')
def is_number(x):
    return isinstance(x, int) or NUMBER.match(x)


def evaluate(expression, circuit, wire):
    match expression:
        case And(x, y):
            left = int(x) if is_number(x) else evaluate(circuit[x], circuit, x)
            right = int(y) if is_number(y) else evaluate(circuit[y], circuit, y)
            circuit[wire] = left & right
            return circuit[wire]
        case Or(x, y):
            left = int(x) if is_number(x) else evaluate(circuit[x], circuit, x)
            right = int(y) if is_number(y) else evaluate(circuit[y], circuit, y)
            circuit[wire] = left | right
            return circuit[wire]
        case Lshift(x, y):
            left = int(x) if is_number(x) else evaluate(circuit[x], circuit, x)
            right = int(y) if is_number(y) else evaluate(circuit[y], circuit, y)
            circuit[wire] = left << right
            return circuit[wire]
        case Rshift(x, y):
            left = int(x) if is_number(x) else evaluate(circuit[x], circuit, x)
            right = int(y) if is_number(y) else evaluate(circuit[y], circuit, y)
            circuit[wire] = left >> right
            return circuit[wire]
        case Not(x):
            value = int(x) if is_number(x) else evaluate(circuit[x], circuit, x)
            circuit[wire] = -value%65535
            return circuit[wire]
        case Same(x):
            return int(x) if is_number(x) else evaluate(circuit[x], circuit, x)
        case int() as value:
            return value
        case _:
            raise Exception("unexpected", expression)


def get_signal(circuit, wire):
    expression = circuit[wire]
    return evaluate(expression, circuit, wire)


if __name__ == '__main__':
    circuit: dict[str, Any] = {}

    for wire in open('input.txt'):
        parse_wire(circuit, wire)

    print(get_signal(circuit, 'a'))
