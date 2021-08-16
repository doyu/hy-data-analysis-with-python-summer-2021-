#!/usr/bin/env python3

import sys
import math
from functools import reduce

def summary(filename):
    with open(filename, "r") as f:
        l = f.read().splitlines()
        l = list(map(float, l))
        total = reduce(lambda a, b : a+b, l)
        ave = total / len(l)
        std = reduce(lambda v, e : v + (e-ave)**2, l)
        std = math.sqrt(std / len(l))
    return (total, ave, std)

def main():
    for f in sys.argv[1:]:
        ret = summary(f)
        # File: src/example.txt Sum: 51.400000 Average: 10.280000 Stddev: 8.904606
        print(f"File: {f} Sum: {ret[0]:0>.6} Average: {ret[1]:.6} Stddev: {ret[2]:.6}")


if __name__ == "__main__":
    main()
