#!/usr/bin/env python3

# Exercise 14 (find matching)
# Write function find_matching that gets a list of strings and a search
# string as parameters. The function should return the indices to those
# elements in the input list that contain the search string. Use the
# function enumerate.
#
# An example:
# find_matching(["sensitive", "engine", "rubbish", "comment"], "en") should return the list [0, 1, 3].

def find_matching(L, pattern):
    ret = []
    for i, x in enumerate(L):
        if pattern in x:
            ret.append(i)
    return ret

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
