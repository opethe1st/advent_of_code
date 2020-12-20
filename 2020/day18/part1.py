from typing import Any


def apply(operator, lvalue, rvalue):
    if operator == '+':
        return lvalue + rvalue
    elif operator == '*':
        return lvalue * rvalue
    else:
        raise Exception("Unknown operator")


def evaluate(expression: list[str], start=0, end_cond=lambda index, expression: index < len(expression) and expression[index] != ')'):
    stack: list[Any] = []
    state = 'NUM'
    index = start
    while end_cond(index, expression):
        token = expression[index]
        if token[0] in '0123456789':
            if state == 'NUM':
                stack.append(int(token))
                index += 1
            elif state == 'OP':
                operator = stack.pop()
                left_value = stack.pop()
                stack.append(apply(operator, left_value, int(token)))
                state = 'NUM'
                index += 1
            else:
                raise Exception()
        elif token[0] in '+*':
            if state == 'NUM':
                stack.append(token)
                state = 'OP'
                index += 1
            elif state == 'OP':
                raise Exception('this should not happen')
            else:
                raise Exception()
        elif token[0] == '(':
            value, index = evaluate(expression, start=index + 1)
            if state == 'NUM':
                state = 'NUM'
                stack.append(value)
                index += 1
            elif state == 'OP':
                operator = stack.pop()
                left_value = stack.pop()
                stack.append(apply(operator, left_value, value))
                state = 'NUM'
                index += 1
        else:
            raise Exception()
        print(stack)

    return stack[0], index



if __name__ == '__main__':
    total = 0
    for expression_string in open('input.txt'):
        value, _ = evaluate(expression_string.replace('(', '( ').replace(')', ' )').split())
        total += value
    print(total)
