from dataclasses import dataclass


@dataclass
class Dimension:
    x: int
    y: int
    z: int


def parse_dimensions(dimension: str) -> Dimension:
    x, y, z = map(int, dimension.split("x"))
    return Dimension(x, y, z)


def wrapping_paper_size(dimension: Dimension) -> int:
    area_side1, area_side2, area_side3 = (
        dimension.x * dimension.y,
        dimension.x * dimension.z,
        dimension.y * dimension.z,
    )
    return 2 * (area_side1 + area_side2 + area_side3) + min(
        area_side1, area_side2, area_side3
    )


if __name__ == "__main__":
    print(
        sum(
            wrapping_paper_size(parse_dimensions(dimension=dimension))
            for dimension in open("input.txt")
        )
    )
