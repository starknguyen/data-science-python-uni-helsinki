#!/usr/bin/env python3

import pandas as pd


def subsetting_with_loc():
    df = pd.read_csv("municipal.tsv", sep='\t', index_col="Region 2018",
                     usecols=["Region 2018", "Population",
                              "Share of Swedish-speakers of the population, %",
                              "Share of foreign citizens of the population, %"])
    return df.loc["Akaa": "Äänekoski"]


def main():
    ss = subsetting_with_loc()
    print(ss)


if __name__ == "__main__":
    main()
