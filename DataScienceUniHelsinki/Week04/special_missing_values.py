#!/usr/bin/env python3

import pandas as pd


def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep='\t')
    cond = (df.LW == "New") | (df.LW == "Re")
    df[cond] = None
    df["Pos"] = pd.to_numeric(df["Pos"], errors="coerce")
    df["LW"] = pd.to_numeric(df["LW"], errors="coerce")

    return df[df.Pos > df["LW"]]


def main():
    smv = special_missing_values()
    print(smv.to_string())
    print(smv.shape)


if __name__ == "__main__":
    main()
