#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_red(image):
    return image * np.array([1,0,0])

def to_green(image):
    return image * np.array([0,1,0])

def to_blue(image):
    return image * np.array([0,0,1])

def to_grayscale(image):
    h,w,c = image.shape
    return np.array(list(map(lambda x: (0.2126*x[0]+0.7152*x[1]+0.0722*x[2]),
                             image.reshape(h*w, 3)))).reshape(h,w)

def main():
    painting = plt.imread("src/painting.png")
    plt.imshow(to_grayscale(painting), cmap=plt.cm.gray)
    plt.show()

    plt.subplot(3, 1, 1)
    plt.imshow(to_red(painting))
    plt.subplot(3, 1, 2)
    plt.imshow(to_green(painting))
    plt.subplot(3, 1, 3)
    plt.imshow(to_blue(painting))
    plt.show()

if __name__ == "__main__":
    main()
