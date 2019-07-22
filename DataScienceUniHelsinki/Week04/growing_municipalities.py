#!/usr/bin/env python3

import pandas as pd


def growing_municipalities(df):
    incr = df[df["Population change from the previous year, %"] > 0]
    return len(incr) / len(df)


def main():
    data = pd.read_csv("src/municipal.tsv", sep='\t', index_col="Region 2018")["Akaa": "Äänekoski"]
    grow_prop_percent = growing_municipalities(data) * 100.0
    print(f"Proportion of growing municipalities: {grow_prop_percent:.{1}f}%")


if __name__ == "__main__":
    main()
