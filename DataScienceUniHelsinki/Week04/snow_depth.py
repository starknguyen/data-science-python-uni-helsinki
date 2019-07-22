#!/usr/bin/env python3

import pandas as pd


def snow_depth():
    wh = pd.read_csv("kumpula-weather-2017.csv")
    stats = wh.describe()
    print(stats)
    return stats.loc["max", "Snow depth (cm)"]


def main():
    max_snow_2017 = snow_depth()
    print(f"Max snow depth: {max_snow_2017:.{1}f}")


if __name__ == "__main__":
    main()
