#!/usr/bin/python3
"""
Iterate numbers from 1 to 100 separated by space
For MULTIPLES od 3 PRINT FIZZ
For MULTIPLES of 5 PRINT BUZZ
For MULTIPLES OF BOTH PRINT FIZZBUZZ
Not allowed to use import modules
Use prototype: def fizzbuzz():
"""

def fizzbuzz():
    for num in range(1 - 100):
        if num * 3 and num * 5:
            print("FizzBuzz")
        elif num * 3:
            print("Fizz")
        elif num * 5:
            print("Buzz")
        else:
            print(num)
