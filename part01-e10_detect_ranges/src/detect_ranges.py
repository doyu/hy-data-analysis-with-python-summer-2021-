#!/usr/bin/env python3

# Exercise 10 (detect ranges)
# Create a function named detect_ranges that gets a list of integers as
# a parameter. The function should then sort this list, and transform
# the list into another list where pairs are used for all the detected
# intervals. So 3,4,5,6 is replaced by the pair (3,7). Numbers that are
# not part of any interval result just single numbers. The resulting
# list consists of these numbers and pairs, separated by commas. An
# example of how this function works:
#
# print(detect_ranges([2,5,4,8,12,6,7,10,13]))
# -> [2,4,5,6,7,8,12,10,13]         # sorted
# -> [[2],[4,5,6,7,8],[10],[12,13]] # grouped
# -> [(2,1)(4,9),(10,1),(12,14)]    # ranged
# -> [2,(4,9),10,(12,14)]           # ranged
# Note that the second element of the pair does not belong to the range.
# This is consistent with the way Python’s range function works. You may
# assume that no element in the input list appears multiple times.

def ranged(l):
    ret = []
    for x in l:
        if len(x) == 1:
            ret.append(x[0])
        else:
            ret.append((x[0], x[0]+len(x)))
    return ret

def grouped(l):
    ret = []
    tmp = []
    while l != []:
        x = l.pop(0)
        if tmp == []:
            tmp.append(x)
        elif tmp[-1] + 1 == x:
            tmp.append(x)
        else:
            ret.append(tmp)
            tmp = [x]
    if tmp:
        ret.append(tmp)
    return ret

def detect_ranges(L):
    l = sorted(L[:])
    l = grouped(l)
    l = ranged(l)
    return l

def main():
#    L = [88, 89, 90, 92, 93, 94, 95, 96, 97]
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(sorted(L))
    print(result)
    print("[2,(4,9),10,(12,14)]")

if __name__ == "__main__":
    main()
