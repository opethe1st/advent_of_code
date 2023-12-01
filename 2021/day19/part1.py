# pylint: disable=all
from collections import defaultdict


def get_all_rotations(points):
    '''blah'''
    return [points]


def all_rotations(scanner_report):
    return []


def is_intersect(a, b):
    return False


def difference(a, b):
    return (0, 0, 0)


def get_intersection(a, b):
    return []


def solution(scanner_reports):
    # distance = defaultdict(lambda x: defaultdict(int))
    # scanner_to_points = defaultdict(list)
    beacons = set()
    canonical_scanner_reports = {}
    for i in range(len(scanner_reports)):
        for j in range(i+1, len(scanner_reports)):
            for rotation in all_rotations(scanner_reports[j]):
                intersection = get_intersection(scanner_reports[i], rotation)
                diff = tuple(x-y for x, y in zip(intersection[0][0], intersection[0][1]))
                if len(intersection) >= 12:
                    canonical_scanner_reports[j] = rotation
                    break


    return len(beacons)

if __name__ == '__main__':
    lines = open('input.txt', encoding='utf-8').read()
    scanner_outputs = [
        scanner_output.strip()
        for scanner_output in lines.split('\n\n')
    ]
    scanner_reports = {}
    for i, scanner_output in enumerate(scanner_outputs):
        points = scanner_output.split('\n')
        scanner_reports[i] = [tuple(map(int, point.split(','))) for point in points[1:]]

    print(scanner_reports)
