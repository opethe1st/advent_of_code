from dataclasses import dataclass


@dataclass
class Dimension:
    x: int
    y: int
    z: int


def parse_dimensions(dimension: str) -> Dimension:
    x, y, z = map(int, dimension.split("x"))
    return Dimension(x, y, z)


def ribbon_size(dimension: Dimension) -> int:
    area_side1, area_side2, area_side3 = (
        dimension.x * dimension.y,
        dimension.x * dimension.z,
        dimension.y * dimension.z,
    )
    smallest_perimeter = min(
        2 * (dimension.x + dimension.y),
        2 * (dimension.x + dimension.z),
        2 * (dimension.y + dimension.z),
    )
    bow = dimension.x * dimension.y * dimension.z
    return smallest_perimeter + bow


if __name__ == "__main__":
    print(
        sum(
            ribbon_size(parse_dimensions(dimension=dimension))
            for dimension in open("input.txt")
        )
    )
