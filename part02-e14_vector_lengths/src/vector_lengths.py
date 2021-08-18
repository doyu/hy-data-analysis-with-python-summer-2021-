#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    x = a * a
    x = x.sum(axis=1)
    x = np.sqrt(x)
    return x

def main():
    print(vector_lengths(np.array([[1,2,3],[4,5,6]])))

if __name__ == "__main__":
    main()
