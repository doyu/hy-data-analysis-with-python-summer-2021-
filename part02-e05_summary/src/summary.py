#!/usr/bin/env python3

import sys
import math
from functools import reduce

def str_to_float(l):
    #return map(float, l)
    ret = []
    for el in l:
        try:
            x = float(el)
        except ValueError:
            continue
        ret.append(x)
    return ret

def summary(filename):
    with open(filename, "r") as f:
        l = f.read().splitlines()
        l = str_to_float(l)
        total = reduce(lambda a, b : a+b, l)
        ave = total / len(l)
        std = reduce(lambda v, e : v + (e-ave)**2, l, 0)
        std = math.sqrt(std / (len(l) - 1))
    return (total, ave, std)

def main():
    for f in sys.argv[1:]:
        ret = summary(f)
        # File: src/example.txt Sum: 51.400000 Average: 10.280000 Stddev: 8.904606
        print(f"File: %s Sum: %.06f Average: %.06f Stddev: %.06f" % (f, ret[0], ret[1], ret[2]))


if __name__ == "__main__":
    main()
