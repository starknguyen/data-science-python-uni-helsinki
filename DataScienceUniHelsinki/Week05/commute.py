#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1, 13)))


def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)

    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    hourmin = d["Hour"].str.split(":", expand=True)

    d["Hour"] = hourmin.iloc[:, 0]
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)

    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

    return d


def bicycle_timeseries():
    df = pd.read_csv("Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    cyc_data = split_date(df)

    df["Date"] = pd.to_datetime(cyc_data[["Year", "Month", "Day", "Hour"]],
                                      format='%Y%m%d %H:%M')
    df = df.drop("Päivämäärä", axis=1)
    df = df.set_index("Date")

    return df


def commute():
    bike_ts = bicycle_timeseries()

    wd_gr = bike_ts["2017-08"].groupby([bike_ts["2017-08"].index.weekday]).sum()
    wd_gr.index = range(1, 8)

    return wd_gr


def main():
    cm = commute()
    plt.plot(cm)
    plt.show()


if __name__ == "__main__":
    main()
