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

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')

fizzbuzz()
