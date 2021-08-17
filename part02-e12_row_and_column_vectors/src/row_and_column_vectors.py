#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    return np.split(a, tuple(n for n in range(1, a.shape[0])))

def get_column_vectors(a):
    return np.split(a, tuple(n for n in range(1, a.shape[1])), axis=1)

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
