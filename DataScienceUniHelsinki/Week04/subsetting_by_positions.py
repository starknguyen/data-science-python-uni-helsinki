#!/usr/bin/env python3

import pandas as pd


def subsetting_by_positions():
    df = pd.read_csv("UK-top40-1964-1-2.tsv", sep='\t',
                     usecols=["Title", "Artist"])

    return df.iloc[0:10]


def main():
    top_10 = subsetting_by_positions()
    print(top_10)
    print(f"Shape = {top_10.shape}")


if __name__ == "__main__":
    main()
