

close_to_open = {
    '}': '{',
    ']': '[',
    ')': '(',
    '>': '<'
}

open_to_close = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}

completion_score = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4,
}



def get_completion_string_score(completion_string: str)->int:
    s = 0
    for character in completion_string:
        s *= 5
        s += completion_score[character]
    return s


if __name__ == '__main__':
    incomplete_lines = []
    for line in open('input.txt'):
        line = line.strip()
        stack = []
        for character in line:
            if character not in close_to_open:
                stack.append(character)
            else:
                opening = stack.pop(-1)
                if close_to_open[character] != opening:
                    break
        else:
            incomplete_lines.append(line)

    completion_strings = []
    for line in incomplete_lines:
        stack = []
        for character in line:
            if character not in close_to_open:
                stack.append(character)
            else:
                opening = stack.pop(-1)
                if close_to_open[character] != opening:
                    break
        else:
            completion_strings.append("".join([open_to_close[character] for character in reversed(stack)]))

    completion_string_scores = sorted([get_completion_string_score(string) for string in completion_strings])
    print(completion_string_scores[len(completion_strings)//2])
