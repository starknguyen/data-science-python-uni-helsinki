#!/usr/bin/env python3

import pandas as pd


def clean_space(s):
    return " ".join(s.split())


def cleaning_data():
    wh = pd.read_csv("presidents.tsv", sep="\t")

    wh.President = wh.President.str.split(",").str[::-1].str.join(' ').str.title()
    wh.President = wh.President.apply(lambda s: clean_space(s))

    wh["Vice-president"] = wh["Vice-president"].str.split(",").str[::-1].str.join(' ').str.title()
    wh["Vice-president"] = wh["Vice-president"].apply(lambda s: clean_space(s))

    wh.Start = wh.Start.str.split(expand=True)
    wh.Start = wh.Start.astype(int)
    wh.Last = wh.Last.str.replace("-", "")
    wh.Last = pd.to_numeric(wh.Last, errors="coerce")
    wh.Seasons = wh.Seasons.str.replace("two", "2")
    wh.Seasons = wh.Seasons.astype(int)

    print(wh)
    return wh


def main():
    clean_data = cleaning_data()

    print(clean_data.dtypes)
    print(clean_data.President)
    print(clean_data.Start)
    print(clean_data.Last)
    print(clean_data.Seasons)
    print(clean_data["Vice-president"])


if __name__ == "__main__":
    main()
