from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
X = namedtuple('X', ['distance'])
Y = namedtuple('Y', ['distance'])


def do_fold(dots, fold):
    new_dots = []
    match fold:
        case X() as fold:
            for dot in dots:
                if dot.x > fold.distance:
                    new_dots.append(Point(fold.distance - abs(dot.x-fold.distance), dot.y))
                elif dot.x < fold.distance:
                    new_dots.append(dot)
        case Y() as fold:
            for dot in dots:
                if dot.y > fold.distance:
                    new_dots.append(Point(dot.x, fold.distance - abs(dot.y-fold.distance)))
                elif dot.y < fold.distance:
                    new_dots.append(dot)

    min_x = min(dot.x for dot in new_dots)
    min_y = min(dot.y for dot in new_dots)
    x_adjust, y_adjust = min(min_x, 0), min(min_y, 0)
    new_dots = set([Point(dot.x+x_adjust, dot.y+y_adjust) for dot in new_dots])
    return new_dots



def print_dots(dots):
    max_x = max(dot.x for dot in dots)
    max_y = max(dot.y for dot in dots)
    rows = [[' ' for _ in range(max_y+1)] for _ in range(max_x+1)]
    for dot in dots:
        rows[max_x-dot.x][dot.y] = '#'
    print(
        "\n".join(
            "".join(row) for row in rows
        )
    )

if __name__ == '__main__':
    dots = []
    folds = []
    for line in open('input.txt'):
        if ',' in line:
            x, y = line.split(',')
            dots.append(Point(int(x), int(y)))
        elif "fold" in line:
            _, _, direction = line.split()
            axis, distance = direction.split('=')
            if axis == 'x':
                folds.append(X(int(distance)))
            else:
                folds.append(Y(int(distance)))

    for fold in folds:
        dots = do_fold(dots, fold)
    print_dots(dots)
