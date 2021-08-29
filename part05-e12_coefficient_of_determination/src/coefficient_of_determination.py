#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
import numpy as np

def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep='\t')
    y = df.Y
    X = df.loc[:, 'X1':'X5']
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(X, y)
    scores = [model.score(X, y)]
    for col in X:
        x = X[col].to_numpy().reshape(-1, 1)
        model.fit(x, y)
        scores.append(model.score(x, y))

    return scores

def main():
    scores = coefficient_of_determination()
    titles = "X X1 X2 X3 X4 X5".split()
    for title, score in zip(titles, scores):
        print(f"R2-score with feature(s) {title}: {score:.2f}")

if __name__ == "__main__":
    main()
