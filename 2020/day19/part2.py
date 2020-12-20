import re


def match(rules_dict, key, string):
    # is this correct
    # if not string:
    #     return True, string
    # here
    if rules_dict[key][0] == '"':
        if string and rules_dict[key].strip('"') == string[0]:
            return [string[1:]]
        else:
            # print('{}\t{}'.format(key, repr(string)))
            return []
    else:
        is_match = False
        for alternative in rules_dict[key].strip().split('|'):
            print(repr(alternative.strip()))
            rest = string
            for subrule in alternative.strip().split():
                if re.match(pattern=r'\d+', string=subrule):
                    is_match, rest = match(rules_dict=rules_dict, key=subrule, string=rest)
                    if not is_match:
                        break
            else:
                is_match = True
                break
        return [(is_match, rest)]


if __name__ == '__main__':
    with open('test2.txt') as file:
        content = file.read()
    rules, strings = [val.strip().split('\n') for val in content.split('\n\n')]

    rules_dict = {}
    for rule in rules:
        key, rule = [val.strip() for val in rule.split(':')]
        rules_dict[key] = rule
    count = 0
    for string in ['babbbbaabbbbbabbbbbbaabaaabaaa']:
        is_match, rest = match(rules_dict, '0', string)
        print('1', string, is_match, repr(rest))
        count += bool(is_match and not rest)
    print(count)
