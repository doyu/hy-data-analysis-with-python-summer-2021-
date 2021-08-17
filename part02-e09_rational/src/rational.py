#!/usr/bin/env python3

'''
Exercise 9 (rational)
Create a class Rational whose instances are rational numbers. A new
rational number can be created with the call to the class. For
example, the call r=Rational(1,4) creates a rational number “one
quarter”. Make the instances support the following operations: + - * /
< > == with their natural behaviour. Make the rationals also printable
so that from the printout we can clearly see that they are rational
numbers.
'''

class Rational(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "%f %f" % (self.a, self.b)
    def __mul__(self, x):
        return Rational((self.a * x.a), (self.b * x.b))
    def __truediv__(self, x):
        return Rational((self.a * x.b), (self.b * x.a))
    def __add__(self, x):
        return Rational((self.a * x.b + x.a * self.b), (self.b * x.b))
    def __sub__(self, x):
        return Rational((self.a * x.b - x.a * self.b), (self.b * x.b))
    def __eq__(self, x):
        return (self.a / self.b) == (x.a / x.b)
    def __lt__(self, x):
        return (self.a / self.b) < (x.a / x.b)
    def __gt__(self, x):
        return (self.a / self.b) > (x.a / x.b)

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
