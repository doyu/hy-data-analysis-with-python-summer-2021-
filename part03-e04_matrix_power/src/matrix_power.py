#!/usr/bin/env python3

import numpy as np
from functools import reduce

def matrix_power(a, n):
    if n < 0:
        return reduce(lambda acc, el: acc @ np.linalg.inv(a), np.arange(-n), np.eye(a.shape[0]))
    return reduce(lambda acc, el: acc @ a, np.arange(n), np.eye(a.shape[0]))

def main():
    a = np.array([[1,2],[3,4]])
    print(matrix_power(a, -1))

if __name__ == "__main__":
    main()
