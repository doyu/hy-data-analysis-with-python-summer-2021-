#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():

    independence = pd.Series([np.nan, 1917,1766,1523,np.nan,1992], dtype=float)
    president = pd.Series([None,"Niinistö","Trump",None,"Steinmeier","Putin"], dtype=object)
    df = pd.DataFrame({"Year of independence" : independence, "President" : president})
    df.index = ["United Kingdom","Finland","USA","Sweden","Germany","Russia"]
    return df

def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
