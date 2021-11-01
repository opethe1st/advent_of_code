from itertools import groupby


def look_and_say(seq):
    s = ''
    for k, g in groupby(seq):
        s += str(len(list(g)))
        s += k
    return s


if __name__ == "__main__":
    seq = "1321131112"
    for _ in range(40):
        seq = look_and_say(seq)
    print(len(seq))
