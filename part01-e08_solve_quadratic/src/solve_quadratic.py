#!/usr/bin/env python3

# Exercise 8 (solve quadratic)
# In mathematics, the quadratic equation ax2+bx+c=0ax2+bx+c=0 can be solved with the formula x=−b±b2−4ac√2ax=−b±b2−4ac2a.
#
# Write a function solve_quadratic, that returns both solutions of a generic quadratic as a pair (2-tuple) when the coefficients are given as parameters. It should work like this:
#
# print(solve_quadratic(1,-3,2))
# (2.0,1.0)
# print(solve_quadratic(1,2,1))
# (-1.0,-1.0)
# You may want to use the math.sqrt function from the math module in your solution. Test that your function works in the main function!


import math

def solve_quadratic(a, b, c):
    temp = math.sqrt(b**2-4*a*c)
    return ((-b + temp)/(2*a), (-b - temp)/(2*a))


def main():
    pass
    print(solve_quadratic(1,-3,2))
    # (2.0,1.0)
    print(solve_quadratic(1,2,1))
    # (-1.0,-1.0)

if __name__ == "__main__":
    main()
