#!/usr/bin/env python3

import pandas as pd
import numpy as np

nums = dict(zip(
    "one two three four five six seven eight nine ten".split(),
    [1,2,3,4,5,6,7,8.9,10]))

def cleaning_data():
    df = pd.read_csv('src/presidents.tsv', sep='\t')
    df.Start = df.Start.str.split(expand=True)[0].astype(int)
    df.Last = pd.to_numeric(df.Last, errors="coerce")
    df.Seasons.replace('two', '2', inplace=True)
    df.Seasons = df.Seasons.astype(int)
    df.President.where(~df.President.str.contains(','),
                       (df.President.str.split(',', expand=True)[1] + " "
                        + df.President.str.split(",", expand=True)[0]),
                       axis=0, inplace=True)
    df.President = df.President.str.strip()
    df['Vice-president'].where(~df['Vice-president'].str.contains(','),
                               (df['Vice-president'].str.split(',', expand=True)[1] + " "
                                + df['Vice-president'].str.split(",", expand=True)[0]),
                               axis=0, inplace=True)
ero
    df["Vice-president"] = df["Vice-president"].str.strip()
    df["Vice-president"] = df["Vice-president"].str.title()
    return df

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
