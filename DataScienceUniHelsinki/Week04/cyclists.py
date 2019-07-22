#!/usr/bin/env python3

import pandas as pd


def cyclists():
    wh = pd.read_csv("Helsingin_pyorailijamaarat.csv", sep=";")
    c = wh.dropna(axis=1, how="all")
    d = c.dropna(axis=0, how="all")
    return d


def main():
    cyclist_cleaned_data = cyclists()
    print(cyclist_cleaned_data)


if __name__ == "__main__":
    main()
