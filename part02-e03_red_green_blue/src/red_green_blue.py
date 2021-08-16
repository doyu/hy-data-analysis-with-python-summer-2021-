#!/usr/bin/env python3

'''
Exercise 3 (red green blue)
The file src/rgb.txt contains names of colors and their numerical representations in RGB format. The RBG format allows a color to be represented as a mixture of red, green, and blue components. Each component can have an integer value in the range [0,255]. Each line in the file contains four fields: red, green, blue, and colorname. Each field is separated by some amount of whitespace (tab or space in this case). The text file is formatted to make it print nicely, but that makes it harder to process by a computer. Note that some color names can also contain a space character.

Write function red_green_blue that reads the file rgb.txt from the folder src. Remove the irrelevant first line of the file. The function should return a list of strings. Clean-up the file so that the strings in the returned list have four fields separated by a single tab character (\t). Use regular expressions to do this.

The first string in the returned list should be:

'255\t250\t250\tsnow'

'''

import re

def red_green_blue(filename="src/rgb.txt"):
    ret = []
    with open(filename, "r") as f:
        for line in f:
            mo = re.search(r"^\s{0,2}(\d{1,3})\s+(\d{1,3})\s{1,3}(\d{1,3})\s+(\w.+)", line)
            if mo == None:
                continue
            ret.append(f"{mo.group(1)}\t{mo.group(2)}\t{mo.group(3)}\t{mo.group(4)}")
    return ret


def main():
    with open("src/rgb1.txt", "w") as f:
        for l in red_green_blue():
            f.write(l)

if __name__ == "__main__":
    main()
