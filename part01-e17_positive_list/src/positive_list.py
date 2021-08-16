#!/usr/bin/env python3

'''
Exercise 17 (positive list)
Write a function positive_list that gets a list of numbers as a parameter, and returns a list with the negative numbers and zero filtered out using the filter function.

The function call positive_list([2,-2,0,1,-7]) should return the list [2,1]. Test your function in the main function.
'''

def is_positive(x):
    if x > 0:
        return True

def positive_list(L):
    return list(filter(is_positive, L))


L = [-44,  8, -38 -64,   6, -30, -22,  17,  18,  29, -12, -57,  80, -81,  58,  27,  82,  83,
  70,  -6,  -7,  -8, -77,  75,  58,  79,  61, -86,  84,  64, -89,  71, -32, -57,  31,  29,
  63,  37, -32, -73, -68,  10, -45,  99, -19, -29, -88, -54,  58,  31]

def main():
#    print(positive_list([2,-2,0,1,-7]))
    print(positive_list(L))

if __name__ == "__main__":
    main()
