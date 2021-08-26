#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv',
                     sep=';')["Päivämäärä"].str.split(expand=True)
    df = df.dropna(how='all')
    df.columns=['Weekday', 'Day', 'Month', 'Year', 'Hour']
    df.Weekday.replace(
        ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su'],
        ['Mon', 'Tue','Wed', 'Thu', 'Fri', 'Sat', 'Sun'], inplace=True)
    df.Month.replace(
        ['tammi', 'helmi', 'maalis','huhti','touko','kesä', 'heinä','elo','syys','loka','marras','joulu'],
        [1,2,3,4,5,6,7,8,9,10,11,12], inplace=True)
    df.Hour = df.Hour.str.split(':', expand=True)[0].astype(int)

    return df.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

def main():
    print(split_date())
# ke 1 tammi 2014 00:00 to Wed 1 1 2014 0

if __name__ == "__main__":
    main()
