#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from functools import reduce

def explained_variance():
    df = pd.read_csv('src/data.tsv', sep='\t')
    pca = PCA()
    pca.fit(df)
    return pd.DataFrame.var(df), pca.explained_variance_

def main():
    v, ev = explained_variance()
    print(f"The variances are: ", " ".join([f"{x:.3f}" for x in v]))
    print(f"The explained variances after PCA are: ", " ".join([f"{x:.3f}" for x in ev]))
    plt.plot(np.arange(1,11), np.cumsum(ev))
    plt.show()

if __name__ == "__main__":
    main()
