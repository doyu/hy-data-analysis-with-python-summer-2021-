#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    plt.subplot(1, 2, 1)    # Note the 1-indexing of subplots.
    plt.plot(a[:,0], a[:,1])
    plt.subplot(1, 2, 2)
    plt.scatter(a[:,0], a[:,1], c=a[:,2], s=a[:,3])
    plt.show()

def main():
#    a = np.array([[1,2,3],[2,3,1],"r",50])
    n = 10
    a = np.random.randint(0, 10, (n, 3))
    a = np.concatenate([np.arange(n)[:, np.newaxis], a], axis=1)
    print(a)
    subfigures(a)

if __name__ == "__main__":
    main()
