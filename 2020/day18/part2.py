
def evaluate(expression):
    pass


if __name__ == '__main__':
    total = 0
    for expression_string in open('input.txt'):
        value, _ = evaluate(expression_string.replace('(', '( ').replace(')', ' )').split())
        total += value
    print(total)
