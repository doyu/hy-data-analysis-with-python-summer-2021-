#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(np.vstack([x]).T, y)
    return model.coef_[0],  model.intercept_

def main():
    train_x = np.linspace(-5,5,10)
    train_y = 1.0 * train_x + np.random.randn(len(train_x))
    slope, intercept = fit_line(train_x, train_y)
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")

    plt.scatter(train_x, train_y, color='black')
    test_x = np.linspace(-5,5,100)
    test_y = test_x * slope + intercept
    plt.plot(test_x, test_y)
    plt.show()

if __name__ == "__main__":
    main()
