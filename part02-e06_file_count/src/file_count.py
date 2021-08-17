#!/usr/bin/env python3

'''
Exercise 6 (file count)
This exercise can give two points at maximum!

Part 1.

Create a function file_count that gets a filename as parameter and returns a triple of numbers. The function should read the file, count the number of lines, words, and characters in the file, and return a triple with these count in this order. You get division into words by splitting at whitespace. You don’t have to remove punctuation.

Part 2.

Create a main function that in a loop calls file_count using each filename in the list of command line parameters sys.argv[1:] as a parameter, in turn. For call python3 src/file_count file1 file2 ... the output should be

?      ?       ?       file1
?      ?       ?       file2
...
The fields are separated by tabs (\t). The fields are in order: linecount, wordcount, charactercount, filename.


'''

import sys
import re
from functools import reduce

def file_count(filename):
    with open(filename, "r") as f:
        buf = f.readlines()
        return (len(buf),
                reduce(lambda a, b: a + len(re.findall(r'\S+', b)), buf, 0),
                reduce(lambda a, b: a+len(b), buf, 0))

def main():
    for f in sys.argv[1:]:
        ret = file_count(f)
        print("%d\t%d\t%d\t%s" % (ret[0], ret[1], ret[2], f))

if __name__ == "__main__":
    main()
