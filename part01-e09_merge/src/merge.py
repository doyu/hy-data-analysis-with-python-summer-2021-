#!/usr/bin/env python3

# Exercise 9 (merge)
# Suppose we have two lists L1 and L2 that contain integers which are
# sorted in ascending order. Create a function merge that gets these
# lists as parameters and returns a new sorted list L that has all the
# elements of L1 and L2. So, len(L) should equal to len(L1)+len(L2). Do
# this using the fact that both lists are already sorted. You can’t use
# the sorted function or the sort method in implementing the merge
# method. You can however use these sorted in the main function for
# creating inputs to the merge function. Test with a couple of examples
# in the main function that your solution works correctly.
#
# Note: In Python argument lists are passed by reference to the
# function, they are not copied! Make sure you don’t modify the original
# lists of the caller.

# https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%BC%E3%82%B8

def merge(L1, L2):
    l1, l2, L = L1[:], L2[:], []
    while True:
        if l1 == []:
            break;
        if l2 == []:
            break;
        if l1[0] < l2[0]:
            L.append(l1.pop(0))
        else:
            L.append(l2.pop(0))

    if l1:
        L.extend(l1)
    if l2:
        L.extend(l2)

    return L

def main():
    a = [1, 3, 5, 7]
    b = [1, 3, 6, 6, 7]
    print(merge(a, b))
    #[6, 1, 7, 3, 6]

if __name__ == "__main__":
    main()
