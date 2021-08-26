#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    orig_columns = df.columns
    re_or_new = (df["LW"] == "Re") | (df["LW"] == "New")
    df = df[~re_or_new]
    df.LW = df.LW.astype(int)
    second_time = df["WoC"] == 2
    on_the_peak_last_week = second_time & ((df.Pos < df["Peak Pos"]) | (df["Peak Pos"] == 40))
    last_week = df.copy()
    last_week.Pos = df.LW
    last_week.LW = df.where(on_the_peak_last_week)["Peak Pos"]
    last_week.WoC = df.WoC - 1
    last_week["Peak Pos"] = df["Peak Pos"].where((df.Pos != df["Peak Pos"]) |
                                                 ((df.Pos == df["Peak Pos"]) &
                                                  (df.LW == df["Peak Pos"])),
                                                 df.LW.where(df.WoC == 2))
    #print(df)
    #print(df.dtypes)
    s = set(range(1, 41)).difference(set(last_week.Pos))
    unknown = pd.DataFrame(list(s), columns=["Pos"])
    #print(unknown)
    version = list(map(int, pd.__version__.split(".")))
    if version[0] == 0 and version[1] < 23:   # older Pandas versions don't support sort option
        last_week = pd.concat([last_week, unknown], ignore_index=True)
    else:
        last_week = pd.concat([last_week, unknown], ignore_index=True, sort=False)
    last_week = last_week[orig_columns]
    return last_week.sort_values(by="Pos", axis=0)

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
