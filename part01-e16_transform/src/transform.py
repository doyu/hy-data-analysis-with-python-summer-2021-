#!/usr/bin/env python3

# Write a function transform that gets two strings as parameters and
# returns a list of integers. The function should split the strings into
# words, and convert these words to integers. This should give two lists
# of integers. Then the function should return a list whose elements are
# multiplication of two integers in the respective positions in the
# lists. For example transform("1 5 3", "2 6 -1") should return the list
# of integers [2, 30, -3].
#
# You have to use split, map, and zip functions/methods. You may assume
# that the two input strings are in correct format.



def transform(s1, s2):
    if len(s1) == 0 | len(s2) == 0:
        return []
    l1 = s1.split(" ")
    l2 = s2.split(" ")
    n1 = map(int, l1)
    n2 = map(int, l2)
    return [x * y for x, y in zip(n1, n2)]

def main():
#    print(transform("1 5 3", "2 6 -1"))
    print(transform("", ""))
    pass

if __name__ == "__main__":
    main()
