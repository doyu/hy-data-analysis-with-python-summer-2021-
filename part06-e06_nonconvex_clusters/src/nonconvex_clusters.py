#!/usr/bin/env python3

'''Exercise 6 (nonconvex clusters)
Read the tab separated file "data.tsv" from the src folder into a
DataFrame. The dataset has two features X1 and X2, and the label y.
Cluster the feature matrix using DBSCAN with different values for the
eps parameter. Use values in np.arange(0.05, 0.2, 0.05) for
clustering. For each clustering, collect the accuracy score, the
number of clusters, and the number of outliers. Return these values in
a DataFrame, where columns and column names are as in the below
example.

Note that DBSCAN uses label -1 to denote outliers , that is, those
data points that didn’t fit well in any cluster. You have to modify
the find_permutation function to handle this: ignore the outlier data
points from the accuracy score computation. In addition, if the number
of clusters is not the same as the number of labels in the original
data, set the accuracy score to NaN.

     eps   Score  Clusters  Outliers
0    0.05      ?         ?         ?
1    0.10      ?         ?         ?
2    0.15      ?         ?         ?
3    0.20      ?         ?         ?
Before submitting the solution, you can plot the data set (with
clusters colored) to see what kind of data we are dealing with.

Points are given for each correct column in the result DataFrame.
'''

import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)

    return permutation

def nonconvex_clusters():
    df = pd.read_csv("src/data.tsv", sep='\t')
    y = df.y
    X = df.iloc[:,:2]
    df2 = pd.DataFrame(columns=["eps", "Score", "Clusters", "Outliers"])
    for eps in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(eps=eps)
        model.fit(X)
        n_clusters = np.unique(model.labels_[model.labels_ != -1]).size
        if np.unique(y).size != n_clusters:
            acc = np.nan
        else:
            permutation = find_permutation(np.unique(y).size, y, model.labels_)
            acc = accuracy_score(y[model.labels_ != -1],
                                 [permutation[x] for x in model.labels_[model.labels_ != -1]])

        df2 = df2.append({"eps":eps, "Score":acc, "Clusters":n_clusters,
                          "Outliers":(model.labels_==-1).sum()},
                         ignore_index=True)
    return df2

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
