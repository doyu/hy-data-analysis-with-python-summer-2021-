#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math

def center(a):
    return  ((a.shape[0]-1)/2, (a.shape[1]-1)/2)

def radial_distance(a):
    yc, xc = center(a)
    ret = np.array([math.sqrt((y-yc)**2 + (x-xc)**2)
                    for x in range(a.shape[1])
                    for y in range(a.shape[0])]).reshape(a.shape[:2])
    return ret

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
    [tmin,tmax]."""
    old_range = a.max() - a.min()
    if old_range == 0:
        return a
    new_range = tmax - tmin
    return (a - a.min()) *  new_range / old_range + tmin

def radial_mask(a):
    ret = 1 - scale(radial_distance(a))
    return np.where(ret < 1.0, 1.0, ret)

def radial_fade(a):
    return a * radial_mask(a)[:,:,np.newaxis]

def main():
    painting = plt.imread("src/painting.png")
    img = painting.copy()
    fig, ax = plt.subplots(3,1)
    ax[0].imshow(painting)
    ax[1].imshow(radial_mask(img))
    ax[2].imshow(radial_fade(img))
    plt.show()

if __name__ == "__main__":
    main()
