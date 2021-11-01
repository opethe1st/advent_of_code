

def count_characters_in_memory(s: str) -> int:
    i = 0
    count = 0
    while i < len(s):
        if s[i:i+2] == r'\\':
            i += 2
        elif s[i:i+2] == r'\"':
            i += 2
        elif s[i:i+2] == r'\x':
            i += 4
        else:
            i += 1
        count += 1
    return count


if __name__ == "__main__":
    total_characters_in_code = 0
    total_characters_in_memory = 0
    # for string in ['""', '"abc"', r'"aaa\"aaa"', r'"\x27"']:
    for string in open('input.txt'):
        total_characters_in_code += len(string)
        total_characters_in_memory += count_characters_in_memory(string[1:-1])
    print(total_characters_in_code-total_characters_in_memory)
