#!/usr/bin/env python3

'''
Copy the function suicide fractions from the previous exercise.

Implement function suicide_weather as described below. We use the
dataset of average temperature (over years 1961-1990) in different
countries from
src/List_of_countries_by_average_yearly_temperature.html
(https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature)
. You can use the function pd.read_html to get all the tables from a
html page. By default pd.read_html does not know which row contains
column headers and which column contains row headers. Therefore, you
have to give both index_col and header parameters to read_html. Maku
sure you use the country as the (row) index for both of the
DataFrames. What is the Spearman correlation between these variables?
Use the corr method of Series object. Note the the two Series need not
be sorted as the indices of the rows (country names) are used to align
them.

The return value of the function suicide_weather is a tuple
(suicide_rows, temperature_rows, common_rows, spearman_correlation)
The output from the main function should be of the following form:

'''

import pandas as pd

def temperatures():
    df = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", header= 0, index_col=0)[0]
    df.iloc[:,0] = df.iloc[:,0].str.replace("\u2212", "-").astype(float)
    return df

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv", sep=',')
    df = df[['country','suicides_no', 'population']]
    return df.groupby('country').apply(lambda x: (x.suicides_no / x.population).mean())

def suicide_weather():
    df1 = suicide_fractions()
    df1.name = "Suicide Fractions"
    df2 = temperatures()
    df = pd.merge(df1, df2, left_index=True, right_index=True)
    #    return df1.shape[0], df2.shape[0], df.shape[0], df['Suicide Fractions'].corr(df.iloc[:,1], method="spearman")
    return df1.shape[0], df2.shape[0], df.shape[0], df.corr("spearman")

def main():
    info = suicide_weather()
    print(f"Suicide DataFrame has {info[0]} rows")
    print(f"Temperature DataFrame has {info[1]} rows")
    print(f"Common DataFrame has {info[2]} rows")
    print(f"Spearman correlation: {info[3]}")

if __name__ == "__main__":
    main()
