#!/usr/bin/env python3

'''
Exercise 6 (suicide fractions)

Load the suicide data set from src folder. This data was originally
downloaded from Kaggle. Kaggle contains lots of interesting open data
sets.

Write function suicide_fractions that loads the data set and returns a
Series that has the country as the (row) index and as the column the
mean fraction of suicides per population in that country. In other
words, the value is the average of suicide fractions. The information
about year, sex and age is not used.
'''

import pandas as pd
import numpy as np

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv", sep=',')
    df = df[['country','suicides_no', 'population']]
    return df.groupby('country').apply(lambda x: (x.suicides_no / x.population).mean())



def main():
    print(suicide_fractions())

if __name__ == "__main__":
    main()
