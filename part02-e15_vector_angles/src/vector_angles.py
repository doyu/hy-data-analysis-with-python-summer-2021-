#!/usr/bin/env python3

import math
import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    a = np.sum(X * Y) / (scipy.linalg.norm(X) * scipy.linalg.norm(Y))
    return np.rad2deg(np.arccos(np.clip(a, -1.0, 1.0)))

def main():
    A=np.array([[0,0,1], [-1,1,0]])
    B=np.array([[0,1,0], [1,1,0]])
    print(vector_angles(A, B))

if __name__ == "__main__":
    main()
