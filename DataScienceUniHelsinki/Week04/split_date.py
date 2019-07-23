#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    wh = pd.read_csv("Helsingin_pyorailijamaarat.csv", sep=";")
    wh = wh.dropna(axis=1, how="all")
    wh = wh.dropna(axis=0, how="all")
    wh = wh["Päivämäärä"].str.split(expand=True)
    wh.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    wh.Hour = wh.Hour.str.split(":", expand=True)

    weekdays_dict = {"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"}
    month_dict = {"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8,
                  "syys": 9, "loka": 10, "marras": 11, "joulu": 12}

    wh.Weekday = wh.Weekday.map(weekdays_dict)
    wh.Month = wh.Month.map(month_dict).values.astype(int)

    wh = wh.astype({"Day": int, "Month": int, "Year": int, "Hour": int})

    return wh


def main():
    sd = split_date()
    print(sd)


if __name__ == "__main__":
    main()
