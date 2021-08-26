#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    df = pd.DataFrame(s, columns=[1], index=s.index)
    for i in range(2, k+1):
        df[i] = pd.DataFrame(s**i, columns=[i], index=s.index)
    return df

def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 5))

#    1   2   3
# a  1   1   1
# b  2   4   8
# c  3   9  27
# d  4  16  64

if __name__ == "__main__":
    main()
