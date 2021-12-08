def get_segments_with_length(segments, length):
    return list(filter(lambda x: len(x) == length, segments))


def get_one(segments):
    return get_segments_with_length(segments, 2)[0]


def get_four(segments):
    return get_segments_with_length(segments, 4)[0]


def get_seven(segments):
    return get_segments_with_length(segments, 3)[0]


def get_eight(segments):
    return get_segments_with_length(segments, 7)[0]


def get_three(one, five_sized_segments):
    for segment in five_sized_segments:
        if len(set(segment) - set(one)) == 3:
            return segment


def get_six(one, six_sized_segments):
    for segment in six_sized_segments:
        if len(set(segment) - set(one)) == 5:
            return segment


def get_five(six, five_sized_segments):
    for segment in five_sized_segments:
        if len(set(segment) | set(six)) == 6:
            return segment


def get_two(five, three, five_size_segments):
    five_size_segments.remove(five)
    five_size_segments.remove(three)
    return five_size_segments[0]


def get_nine(three, possible_zero_or_nine):
    for zero_or_nine in possible_zero_or_nine:
        if len(set(zero_or_nine) - set(three)) == 1:
            return zero_or_nine


def convert_to_int(digits: list[int]):
    s = 0
    for digit in digits:
        s *= 10
        s += digit
    return s

def solution(segments, digits):
    one = get_one(segments)
    four = get_four(segments)
    seven = get_seven(segments)
    eight = get_eight(segments)

    five_sized_segments = get_segments_with_length(segments, 5)
    six_sized_segments = get_segments_with_length(segments, 6)

    three = get_three(one, five_sized_segments)
    six = get_six(one, six_sized_segments)
    five = get_five(six, five_sized_segments)
    two = get_two(five, three, five_sized_segments)

    six_sized_segments.remove(six)

    possible_zero_or_nine = six_sized_segments
    nine = get_nine(three, possible_zero_or_nine)

    possible_zero_or_nine.remove(nine)
    zero = possible_zero_or_nine[0]

    segment_to_int = {
        "".join(sorted(one)): 1,
        "".join(sorted(two)): 2,
        "".join(sorted(three)): 3,
        "".join(sorted(four)): 4,
        "".join(sorted(five)): 5,
        "".join(sorted(six)): 6,
        "".join(sorted(seven)): 7,
        "".join(sorted(eight)): 8,
        "".join(sorted(nine)): 9,
        "".join(sorted(zero)): 0,
    }
    digits = [segment_to_int["".join(sorted(digit))] for digit in digits]
    return convert_to_int(digits)


if __name__ == "__main__":
    s = 0
    for line in open("input.txt"):
        segments, output = line.split(" | ")
        nums = output.split()
        segments = segments.split()
        s += solution(segments, digits=nums)

    print(s)
