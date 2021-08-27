#!/usr/bin/env python3

import pandas as pd

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
    return pd.concat([p, df.iloc[:,1:]], axis=1)

def weather_data():
    return pd.read_csv('src/kumpula-weather-2017.csv', sep=',')

def cycling_weather():
    return  pd.merge(cycling_data(), weather_data(),
                     left_on=["Year", "Month", "Day"], right_on=["Year", "m", "d"]).drop(
                         ["m", "d", "Time", "Time zone"], axis=1)

def main():
    print(cycling_weather())

if __name__ == "__main__":
    main()
