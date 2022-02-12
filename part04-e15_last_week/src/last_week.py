#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    tw = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    tw = tw.rename(columns={'Peak Pos':'Peak'})
    tw = tw[(tw.LW!="Re") & (tw.LW!="New")]
    tw.LW = tw.LW.astype(int)

    lw = tw.copy()
    lw.Pos = tw.LW

    # Peak at 2 weeks ago -> lw.LW == tw.Peak
    f = lambda x: x.Peak if (x.WoC == 3) & ((x.Pos > x.Peak) & (x.LW > x.Peak)) else np.nan
    lw.LW = tw.apply(f, axis=1)

    # Updating WoC
    lw.WoC -= 1

    # Updating Peak
    def f(r):
        if (r.Pos != r.Peak):
            return r.Peak
        if (r.Pos == r.Peak) & (r.LW == r.Peak):
            return r.Peak 
        if r.WoC==2:
            return r.LW
        return np.nan
    lw.Peak = tw.apply(f, axis=1)
    
    # Adding empty columns
    s = set(range(1, 41)).difference(set(lw.Pos))
    unknown = pd.DataFrame(list(s), columns=["Pos"])
    lw = pd.concat([lw, unknown], ignore_index=True)
    lw = lw.sort_values(by="Pos")

    lw = lw.rename(columns={'Peak':'Peak Pos'})
    return lw

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
