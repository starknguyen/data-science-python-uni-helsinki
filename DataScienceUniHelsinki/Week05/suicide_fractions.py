#!/usr/bin/env python3

import pandas as pd


def suicide_fractions():
    df = pd.read_csv("who_suicide_statistics.csv")
    print(df)

    df["avg"] = df["suicides_no"] / df["population"]
    gr = df.groupby("country")["avg"].mean()

    return gr


def main():
    sf = suicide_fractions()
    print(sf)


if __name__ == "__main__":
    main()
