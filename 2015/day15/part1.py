from math import prod
from dataclasses import dataclass


@dataclass
class Cookie:
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def highest_scoring_cookie():
    cookies = [
        Cookie(5, -1, 0, 0, 5),
        Cookie(-1, 3, 0, 0, 1),
        Cookie(0, -1, 4, 0, 6),
        Cookie(-1, 0, 0, 2, 8)
    ]
    # cookies =[
    #     Cookie(-1, -2, 6, 3, 8),
    #     Cookie(2, 3, -2, -1, 3)
    # ]

    highest_score = 0
    for a in range(101):
        for b in range(101-a):
            for c in range(101-a-b):
                d = 100 - a - b - c
                highest_score = max(
                    highest_score,
                    prod(
                        [
                            max(0, sum(x*y for x,y in zip([a, b, c, d], [cookie.capacity for cookie in cookies]))),
                            max(0, sum(x*y for x,y in zip([a, b, c, d], [cookie.durability for cookie in cookies]))),
                            max(0, sum(x*y for x,y in zip([a, b, c, d], [cookie.flavor for cookie in cookies]))),
                            max(0, sum(x*y for x,y in zip([a, b, c, d], [cookie.texture for cookie in cookies]))),
                            # max(0, sum(x*y for x,y in zip([a, b, c, d], [cookie.calories for cookie in cookies]))),
                        ]
                    )
                )
    return highest_score


if __name__ == '__main__':
    print(highest_scoring_cookie())
