#!/usr/bin/env python3

import numpy as np

def diamond(n):
    x = np.eye(n, dtype=int)
    r = np.concatenate((x[:-1,:], x[::-1]), axis=0)
    return np.concatenate((r.T[::-1].T, r[:,1:]), axis=1)

def main():
    print(diamond(3))
    print(diamond(1))

if __name__ == "__main__":
    main()
