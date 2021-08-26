#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    return df[df['Population change from the previous year, %'] > 0].shape[0] / df.shape[0]

def main():
    df = pd.read_csv("src/municipal.tsv", sep='\t', index_col=0)["Akaa":"Äänekoski"]
    print("Proportion of growing municipalities: {:.1%}".format(growing_municipalities(df)))

if __name__ == "__main__":
    main()
