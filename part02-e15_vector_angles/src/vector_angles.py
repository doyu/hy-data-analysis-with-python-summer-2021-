#!/usr/bin/env python3

import math
import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    a = np.sum(X * Y) / (np.sqrt((X**2).sum()) * np.sqrt((Y**2).sum()))
    return np.arccos(np.clip(a, -1.0, 1.0)) * 360 / (2*np.pi)


def main():
    A=np.array([[0,0,1], [-1,1,0]])
    B=np.array([[0,1,0], [1,1,0]])
    print(vector_angles(A, B))

if __name__ == "__main__":
    main()
