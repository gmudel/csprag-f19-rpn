#!/usr/bin/env python3

import operator
from termcolor import colored

operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
        '^': operator.pow,
        '%': operator.mod,
        }

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)

    if len(stack) != 1:
        raise TypeError("malformed input")
    return colored(arg1, "red"), colored(token, "red"), colored(arg2, "red"), colored("=", "green"), colored(stack.pop(), "green")

def main():
    while True:
        result = calculate(input('rpn calc> '))
        print(result)

if __name__ == '__main__':
    main()
