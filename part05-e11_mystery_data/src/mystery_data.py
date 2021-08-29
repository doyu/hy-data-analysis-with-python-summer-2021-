#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv", sep='\t')
    y = df.Y
    X = df.drop(columns="Y")
    model = LinearRegression(fit_intercept=False)
    model.fit(X, y)
    return model.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    print(f"Coefficient of X1 is {coefficient[0]}")
    print(f"Coefficient of X2 is {coefficient[1]}")
    print(f"Coefficient of X3 is {coefficient[2]}")
    print(f"Coefficient of X4 is {coefficient[3]}")
    print(f"Coefficient of X5 is {coefficient[4]}")

if __name__ == "__main__":
    main()
