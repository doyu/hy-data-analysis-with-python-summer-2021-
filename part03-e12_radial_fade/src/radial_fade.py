#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    ny,nx = a.shape[:2]
    return  ((ny-1)/2, (nx-1)/2)   # note the order: (center_y, center_x)

def radial_distance(a):
    # https://tmc.mooc.fi/paste/fEQWDPKUpxJFUt5BBMc42w
    rows = np.arange(a.shape[0])
    cols = np.arange(a.shape[1])
    y, x = np.meshgrid(rows,cols,indexing='ij')
    yc, xc = center(a)
    dist = (((y-yc)**2) + ((x-xc)**2))**0.5
    return dist

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
    [tmin,tmax]."""
    if (a.max() == a.min()).all:
        return a
    old_range = a.max() == a.min()
    new_range = tmax - tmin
    return (a - a.min()) *  new_range / old_range + tmin

def radial_mask(a):
    dist = radial_distance(a)
    dist_scaled = scale(dist)
    return 1 - dist_scaled

def radial_fade(a):
    return a * radial_mask(a)[:,:,np.newaxis]

def main():
    n = 1
    m = 2
    a = np.random.randn(n,m,3)
    result = radial_fade(a)
    cy = (n-1) // 2
    cx = (m-1) // 2
    print(result[cy,cx])
    print(a[cy,cx])
    assert (result[cy,cx] == a[cy,cx]).all(), "In the center of the image there should be no fading"

#    painting = plt.imread("src/painting.png")
#    plt.subplot(3, 1, 1)
#    plt.imshow(painting)
#    plt.subplot(3, 1, 2)
#    plt.imshow(radial_mask(painting))
#    plt.subplot(3, 1, 3)
#    plt.imshow(radial_fade(painting))
    plt.show()

if __name__ == "__main__":
    main()
