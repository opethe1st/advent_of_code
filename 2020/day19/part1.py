import re


def expand(rules_dict, key):
    if rules_dict[key][0] == '"':
        return rules_dict[key].strip('"')
    else:
        regex = ''
        for subrule in rules_dict[key].split():
            if re.match(pattern=r'\d+', string=subrule):
                regex += "("+expand(rules_dict, subrule)+")"
            else:
                regex += subrule
        return regex


if __name__ == '__main__':
    with open('input.txt') as file:
        content = file.read()
    rules, strings = [val.strip().split('\n') for val in content.split('\n\n')]

    rules_dict = {}
    for rule in rules:
        key, rule = [val.strip() for val in rule.split(':')]
        rules_dict[key] = rule

    regex = expand(rules_dict, '0')
    RE = re.compile('^'+regex+'$')
    count = 0
    for string in strings:
        count += bool(RE.match(string))
    print(count)
