#!/usr/bin/env python3

# Exercise 7 (areas of shapes)
# Create a program that can compute the areas of three shapes,
# triangles, rectangles and circles, when their dimensions are given.
#
# An endless loop should ask for which shape you want the area be
# calculated. An empty string as input will exit the loop. If the user
# gives a string that is none of the given shapes, the message “unknown
# shape!” should be printed. Then it will ask for dimensions for that
# particular shape. When all the necessary dimensions are given, it
# prints the area, and starts the loop all over again. Use format
# specifier f for the area.
#
# What happens if you give incorrect dimensions, like giving string “aa”
# as radius? You don’t have to check for errors in the input.
#
# Example interaction:
#
# Choose a shape (triangle, rectangle, circle): triangle
# Give base of the triangle: 20
# Give height of the triangle: 5
# The area is 50.000000
# Choose a shape (triangle, rectangle, circle): rectangel
# Unknown shape!
# Choose a shape (triangle, rectangle, circle): rectangle
# Give width of the rectangle: 20
# Give height of the rectangle: 4
# The area is 80.000000
# Choose a shape (triangle, rectangle, circle): circle
# Give radius of the circle: 10
# The area is 314.159265
# Choose a shape (triangle, rectangle, circle):


import math

def main():
    # enter you solution here
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == 'triangle':
            b = input("Give base of the triangle: ")
            h = input("Give height of the triangle: ")
            ret = (float(b) * float(h)) / 2.0
            print("The area is %.6f" % ret)
        elif shape == 'rectangle':
            w = input("Give width of the rectangle: ")
            h = input("Give height of the rectangle: ")
            print("The area is %.6f" % (float(w) * float(h)))
        elif shape == 'circle':
            r = input("Give radius of the circle: ")
            print("The area is %.6f" % ((math.pi * float(r) ** 2)))
        elif shape == '':
            return
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
