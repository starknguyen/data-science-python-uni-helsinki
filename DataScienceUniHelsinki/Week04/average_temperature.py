#!/usr/bin/env python3

import pandas as pd


def average_temperature():
    wh = pd.read_csv("kumpula-weather-2017.csv", index_col="m")
    return wh.loc[7, ["Air temperature (degC)"]].mean()[0]


def main():
    avg_temp = average_temperature()
    print(f"Average temperature in July: {avg_temp:.{1}f}")


if __name__ == "__main__":
    main()
