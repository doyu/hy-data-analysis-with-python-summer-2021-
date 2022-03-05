#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model

days = dict(zip("ma ti ke to pe la su".split(),
                "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(),
                  range(1,13)))

def cycling_data():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')
    p = df.Päivämäärä.str.split(expand=True)
    p.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    p.Hour = p.Hour.str.split(":", expand=True)[0]
    p.Weekday, p.Month = p.Weekday.map(days), p.Month.map(months)
    p = p.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    df = pd.concat([p, df.iloc[:,1:]], axis=1)
#    df = df.groupby(["Year", "Month", "Day"]).sum().reset_index()
    df = df.groupby(["Year", "Month", "Day"]).sum()
    return df

def weather_data():
    return pd.read_csv('src/kumpula-weather-2017.csv', sep=',')

def cycling_weather():
    return pd.merge(cycling_data(), weather_data(),
                    left_on=["Year", "Month", "Day"], right_on=["Year", "m", "d"]).drop(
                        ["m", "d", "Time", "Time zone"], axis=1)


def cycling_weather_continues(station):
    df = cycling_weather()
    df = df[df.Year == 2017]
    df = df.fillna(method='ffill')
    X = df.iloc[:,-3:]
    y = df[station]
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(X, y)
    return model.coef_, model.score(X, y)

def main():
    station = "Eteläesplanadi"
    L, score = cycling_weather_continues(station)
    print("Measuring station: {}\nRegression coefficient for variable 'precipitation': {:.1f}\nRegression coefficient for variable 'snow depth': {:.1f}\nRegression coefficient for variable 'temperature': {:.1f}\nScore: {:.2f}".format(station,L[0],L[1],L[2],score)) 

if __name__ == "__main__":
    main()
