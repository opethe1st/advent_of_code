from math import lcm


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def solve(x, y):
    g, m, n = egcd(x, y)
    # print('x, y, gcd, m, n, -', x, y, g, m, n, m*x+n*y)
    return -n


if __name__ == "__main__":
    earliest_time_to_depart = int(input())
    values = [value for value in input().split(",")]
    bus_ids = [int(value) for value in values if value != "x"]
    positions = {int(value): i for i, value in enumerate(values) if value != "x"}

    lowest_common_multiple = lcm(*bus_ids)
    print(
        sum(
            positions[b]
            * solve(b, lowest_common_multiple // b)
            * lowest_common_multiple
            // b
            for b in bus_ids
        )
        % lowest_common_multiple
    )
