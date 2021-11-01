
def convert_to_int(current_password):
    ans = 0
    for i in range(8):
        ans *= 26
        ans += ord(current_password[i]) - ord('a')
    return ans


def convert_to_base(int_rep, base) -> str:
    s = []
    while int_rep:
        d = int_rep%26
        s.append(chr(d+ord('a')))
        int_rep //= 26
    return "".join(reversed(s))


def next_password(current_password: str) -> str:
    int_rep = convert_to_int(current_password)
    return convert_to_base((int_rep+1), 26)


def is_valid_password(password):
    alphabet = 'abcdefgheijklmnopqrstuvwxyz'
    if 'i' in password:
        return False
    if 'o' in password:
        return False
    if 'l' in password:
        return False

    if len({f'{x}{x}' for x in alphabet} & {f'{x}{y}' for x, y in zip(password, password[1:])}) < 2:
        return False

    if not {password[i:i+3] for i in range(len(password)-2)} & {alphabet[i:i+3] for i in range(26)}:
        return False
    return True
if __name__ == '__main__':
    password = 'cqjxjnds'
    while not is_valid_password(password):
        # print(password)
        password = next_password(password)
    print(password)
