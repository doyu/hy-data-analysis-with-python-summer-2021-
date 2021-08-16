#!/usr/bin/env python3

'''
Exercise 2 (file listing)
The file src/listing.txt contains a list of files with one line per file. Each line contains seven fields: access rights, number of references, owner’s name, name of owning group, file size, date, filename. These fields are separated with one or more spaces. Note that there may be spaces also within these seven fields.

Write function file_listing that loads the file src/listing.txt. It should return a list of tuples (size, month, day, hour, minute, filename). Use regular expressions to do this (either match, search, findall, or finditer method).

An example: for line

-rw-r--r-- 1 jttoivon hyad-all   25399 Nov  2 21:25 exception_hierarchy.pdf
the function should create the tuple (25399, "Nov", 2, 21, 25, "exception_hierarchy.pdf").
'''

import re


def file_listing(filename="src/listing.txt"):
    ret = []
    with open(filename, "r") as f:
        for line in f:
            l = line.split()
            l = l[4:]

            mo = re.search(r"(\d\d):(\d\d)", "21:33")
            ret.append(tuple([int(l[0]), l[1], int(l[2]), int(mo.group(1)), int(mo.group(2)),l[4]]))
    return ret

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
