#!/usr/bin/env python3

import pandas as pd


def below_zero():
    wh = pd.read_csv("kumpula-weather-2017.csv", index_col="d")
    return len(wh[wh["Air temperature (degC)"] < 0])


def main():
    ndays_below_zero = below_zero()
    print(f"Number of days below zero: {ndays_below_zero}")


if __name__ == "__main__":
    main()
