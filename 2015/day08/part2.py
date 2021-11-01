

def count_characters_in_string(s: str) -> int:
    i = 0
    count = 0
    while i < len(s):
        if s[i] == "\\":
            count += 2
        elif s[i] == '"':
            count += 2
        else:
            count += 1
        i += 1
    return count + 2


if __name__ == "__main__":
    total_characters_in_code = 0
    total_characters_in_memory = 0
    # for string in [r'"\x27"']:
    for string in open('input.txt'):
        total_characters_in_code += count_characters_in_string(string)
        total_characters_in_memory += len(string)
    print(total_characters_in_code-total_characters_in_memory)
