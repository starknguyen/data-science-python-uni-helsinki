#!/usr/bin/env python3

import pandas as pd


def swedish_and_foreigners():
    df = pd.read_csv("municipal.tsv", sep='\t', index_col="Region 2018")["Akaa": "Äänekoski"]
    swe_speaker_col_name = "Share of Swedish-speakers of the population, %"
    foreign_speaker_col_name = "Share of foreign citizens of the population, %"

    swe_cond = df[swe_speaker_col_name] > 5
    foreign_cond = df[foreign_speaker_col_name] > 5

    swe = df[swe_cond][["Population", swe_speaker_col_name]]
    foreign = df[foreign_cond][["Population", foreign_speaker_col_name]]
    #print(swe)
    #print(swe.shape)
    #print("\n")
    #print(foreign)
    #print(foreign.shape)

    return pd.merge(swe, foreign, on=["Region 2018", "Population"])


def main():
    print(swedish_and_foreigners())


if __name__ == "__main__":
    main()
