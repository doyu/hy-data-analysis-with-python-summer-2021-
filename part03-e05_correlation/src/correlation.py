#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    d = load()
    cr = scipy.stats.pearsonr(d[:,0], d[:,2])[0]
    return cr

def correlations():
    d = load()
    return np.corrcoef(d, rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
