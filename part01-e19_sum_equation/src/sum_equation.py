#!/usr/bin/env python3
'''
Exercise 19 (sum equation)
Write a function sum_equation which takes a list of positive integers as parameters and returns a string with an equation of the sum of the elements.

Example: sum_equation([1,5,7]) returns "1 + 5 + 7 = 13" Observe, the spaces should be exactly as shown above. For an empty list the function should return the string “0 = 0”.
'''

from functools import reduce   # import the reduce function from the functools module


def sum_equation(L):
    if L == []:
        return "0 = 0"
    return " = ".join([" + ".join(map(str, L)), str(reduce(lambda x,y:x+y, L, 0))])

def main():
    print(sum_equation([1,5,7]))


if __name__ == "__main__":
    main()
