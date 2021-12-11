
from os import close


close_to_open = {
    '}': '{',
    ']': '[',
    ')': '(',
    '>': '<'
}

syntax_error_score = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137,
}

if __name__ == '__main__':
    illegal_characters = []
    for line in open('input.txt'):
        stack = []
        for item in line:
            if item not in close_to_open:
                stack.append(item)
            else:
                opening = stack.pop(-1)
                if close_to_open[item] != opening:
                    illegal_characters.append(item)
                    break

    print(sum(syntax_error_score[character] for character in illegal_characters))
