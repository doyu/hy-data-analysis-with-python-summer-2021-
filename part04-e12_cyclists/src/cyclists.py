#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    x = df.dropna(how='all', axis=1)
    return x.dropna(how='all')


def main():
    return
    
if __name__ == "__main__":
    main()
