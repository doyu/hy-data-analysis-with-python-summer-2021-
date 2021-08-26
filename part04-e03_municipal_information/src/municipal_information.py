#!/usr/bin/env python3

import pandas as pd

def main():
    df = pd.read_csv("src/municipal.tsv", sep='\t')
    print("Shape: %d,%d" % (df.shape[0],  df.shape[1]))
    print("Columns:")
    for x in df.columns:
        print(x)


if __name__ == "__main__":
    main()
