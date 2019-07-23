#!/usr/bin/env python3

import pandas as pd
import numpy as np


def last_week():
    df = pd.read_csv("UK-top40-1964-1-2.tsv", sep='\t')
    #print(df.to_string())

    df["Pos"] = df["LW"]
    df["LW"] = np.nan

    """
    df_extract = df[nan_cond]
    print("\n")
    print(df_extract.to_string())
    """

    df["WoC"] = pd.to_numeric(df["WoC"], errors="coerce")
    df["WoC"] = df["WoC"] - 1

    df["Pos"] = pd.to_numeric(df["Pos"], errors="coerce")

    co = df["Title"] == "I'M IN LOVE"
    df.loc[co, "Pos"] = 35
    co = df["Title"] == "RUN RUDOLF RUN"
    df.loc[co, "Pos"] = 38
    co = df["Title"] == "DO YOU REALLY LOVE ME TOO?"
    df.loc[co, "Pos"] = 39
    co = df["Title"] == "WALKING ALONE"
    df.loc[co, "Pos"] = 40

    df = df.sort_values(by='Pos')

    df["Pos"] = pd.to_numeric(df["Pos"], errors="coerce")
    df["Peak Pos"] = pd.to_numeric(df["Peak Pos"], errors="coerce")

    nan_cond = ((df["Peak Pos"] < df["Pos"]) & (df["Peak Pos"] > df.index))
    df.loc[nan_cond, ["Peak Pos"]] = np.nan

    nan_cond = ((df["Pos"].isnull()) | (df["WoC"] <= 1))
    df.loc[nan_cond, ["Title", "Artist", "Publisher", "Peak Pos", "WoC"]] = np.nan

    print("\n\n\n")
    print(df.to_string())

    return df


def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
