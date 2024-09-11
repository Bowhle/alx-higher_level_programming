#!/usr/bin/python3

def print_last_digit(number):
    # Compute the last digit
    last_digit = abs(number) % 10
    # Handle negative numbers by adjusting the sign of the last digit
    if number < 0:
        last_digit = -last_digit
    # Print the last digit
    print(last_digit, end="")
    # Return the last digit
    return last_digit
