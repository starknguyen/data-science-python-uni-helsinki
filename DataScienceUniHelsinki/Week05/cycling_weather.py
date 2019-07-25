#!/usr/bin/env python3

import pandas as pd


def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]

    weekdays_dict = {"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"}
    month_dict = {"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8,
                  "syys": 9, "loka": 10, "marras": 11, "joulu": 12}

    d["Weekday"] = d["Weekday"].map(weekdays_dict)
    d["Month"] = d["Month"].map(month_dict)

    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d


def split_date_continues():
    wh = pd.read_csv("Helsingin_pyorailijamaarat.csv", sep=";")
    wh = wh.dropna(axis=1, how="all")
    wh = wh.dropna(axis=0, how="all")

    sd = split_date(wh)
    df = wh.drop("Päivämäärä", axis=1)

    rv = pd.concat([sd, df], axis=1)

    return rv


def cycling_weather():
    cd = split_date_continues()
    wh = pd.read_csv("kumpula-weather-2017.csv")

    df = pd.merge(cd, wh, left_on=["Year", "Day", "Month"], right_on=["Year", "d", "m"], how="inner")
    print(df.shape)

    return df.drop(["d", "m", "Time", "Time zone"], axis=1)


def main():
    cw = cycling_weather()
    print(cw)


if __name__ == "__main__":
    main()
