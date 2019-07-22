#!/usr/bin/env python3

import pandas as pd


def municipalities_of_finland():
    return pd.read_csv("municipal.tsv", sep='\t', index_col="Region 2018")["Akaa": "Äänekoski"]


def main():
    df = municipalities_of_finland()
    print(df)


if __name__ == "__main__":
    main()
