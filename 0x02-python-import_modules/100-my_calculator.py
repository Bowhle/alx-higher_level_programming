#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    num_args = len(argv)

    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    try:
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print(f"{a} {operator} {b} = {result}")


if __name__ == "__main__":
    main()
