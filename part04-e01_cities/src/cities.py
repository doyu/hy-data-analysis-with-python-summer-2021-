#!/usr/bin/env python3

'''
                 Population Total area
Helsinki         643272     715.48
Espoo            279044     528.03
Tampere          231853     689.59
Vantaa           223027     240.35
Oulu             201810     3817.52

'''

import pandas as pd
import numpy as np

def cities():
    population = [
        643272,
        279044,
        231853,
        223027,
        201810
    ]
    area = [
        715.48,
        528.03,
        689.59,
        240.35,
        3817.52
    ]
    idx = [
        "Helsinki",
        "Espoo",
        "Tampere",
        "Vantaa",
        "Oulu"
    ]
    cols = ["Population", "Total area"]
    x = np.array([population,area])
    print(x.shape)
    return pd.DataFrame(x.T, columns=cols, index=idx)

def main():
    print(cities())

if __name__ == "__main__":
    main()
