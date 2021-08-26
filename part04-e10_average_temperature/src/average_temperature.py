#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    df = df[df['m']==7]
    x = df.describe()
    return x.loc['mean', 'Air temperature (degC)']

def main():
    x = average_temperature()
    print(f"Average temperature in July: {x:.1f}")

if __name__ == "__main__":
    main()
