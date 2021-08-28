#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

weekdays_nr = dict(zip("Mon Tue Wed Thu Fri Sat Sun".split(), range(1,8)))
weekdays = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))


def bicycle_timeseries():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(how='all', axis=0).dropna(how='all', axis=1)

    p = df.Päivämäärä.str.split(expand=True)
    p.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    p.Hour = p.Hour.str.split(':', expand=True)[0]
    p.Weekday, p.Month = p.Weekday.map(weekdays), p.Month.map(months)
    p = p.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    p["Date"] = pd.to_datetime(p[["Year", "Month", "Day", "Hour"]])
    df = pd.concat([p, df.iloc[:,1:]], axis=1)
    df.index = df.Date

    return df.drop(["Date", "Day", "Month", "Year", "Hour"], axis=1)


def commute():
    df = bicycle_timeseries()
    df = df.loc["2017-08-01":"2017-08-31", :]
    df.Weekday = df.Weekday.map(weekdays_nr)
    df = df.astype({"Weekday": int})
    df = df.groupby("Weekday").sum()
    return df

def main():
    df = commute()
    df.plot()
    weekdays = "x mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)
    plt.show()

if __name__ == "__main__":
    main()
