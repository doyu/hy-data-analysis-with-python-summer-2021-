#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    x = np.split(a, 2, axis=1)
    c = (np.sum(x[0], axis=1) - np.sum(x[1], axis=1)) > 0
    return a[c]

def main():
    a = np.array([[1, 3, 4, 2],
                  [2, 2, 1, 2]])

    print(first_half_second_half(a))
    # array([[2, 2, 1, 2]])


if __name__ == "__main__":
    main()
