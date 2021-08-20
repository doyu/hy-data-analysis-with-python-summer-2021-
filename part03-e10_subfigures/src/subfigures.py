#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    plt.subplot(1, 2, 1)    # Note the 1-indexing of subplots.
    plt.plot(a[:,0], a[:,1], c=a[:,2])
    plt.subplot(1, 2, 2)
    plt.scatter(a[:,0], a[:,1], c=a[:,2], s=a[:,3])
    plt.show()

def main():
    subfigures(np.random.random((30,4)))

if __name__ == "__main__":
    main()
