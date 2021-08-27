#!/usr/bin/env python3

import pandas as pd


def split_date(df):
    df = df.str.split(expand=True)
    df.columns=['Weekday', 'Day', 'Month', 'Year', 'Hour']
    df.Weekday.replace(
        ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su'],
        ['Mon', 'Tue','Wed', 'Thu', 'Fri', 'Sat', 'Sun'], inplace=True)
    df.Month.replace(
        ['tammi', 'helmi', 'maalis','huhti','touko','kesä', 'heinä','elo','syys','loka','marras','joulu'],
        [1,2,3,4,5,6,7,8,9,10,11,12], inplace=True)
    df.Hour = df.Hour.str.split(':', expand=True)[0].astype(int)

    return df.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})


def split_date_continues():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df.dropna(how='all', inplace=True)
    df.dropna(how='all', axis=1, inplace=True)
    a = split_date(df.Päivämäärä)
    b = df.drop('Päivämäärä', axis=1)
    return pd.concat([a, b], axis=1)


def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
