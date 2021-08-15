#!/usr/bin/env python3

# Exercise 12 (distinct characters)
# Write function distinct_characters that gets a list of strings as a
# parameter. It should return a dictionary whose keys are the strings of
# the input list and the corresponding values are the numbers of
# distinct characters in the key.
#
# Use the set container to temporarily store the distinct characters in
# a string. Example of usage: distinct_characters(["check", "look",
#                                                  "try", "pop"]) should
# return { "check" : 4, "look" : 3, "try" : 3, "pop" : 2}.


def distinct_characters(L):
    l = L[:]
    d = {}
    while l != []:
        x = l.pop(0)
        d[x] = len(set(list(x)))
    return d

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
