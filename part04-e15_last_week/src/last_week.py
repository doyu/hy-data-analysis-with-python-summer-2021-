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
    on_the_peak_llw = (tw.WoC == 3) & ((tw.Pos > tw.Peak) & (tw.LW > tw.Peak))
    lw.LW = np.where(on_the_peak_llw, tw.Peak, np.nan)

    # Updating WoC
    lw.WoC -= 1

    # Updating Peak
    c1 = (tw.Pos != tw.Peak) # Peak was not in this week -> lw.Peak==th.Peak
    c2 = (tw.Pos == tw.Peak) & (tw.LW == tw.Peak) # th.Pos==tw.LW==tw.Peak -> lw.Peak==th.Peak
    lw.Peak = np.where(c1|c2, tw.Peak,
                       np.where(tw.WoC==2, tw.LW, np.nan)) # Otherwise, tw.LW if WoC==2 else don't know
    
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
