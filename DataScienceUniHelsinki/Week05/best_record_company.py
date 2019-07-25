#!/usr/bin/env python3

import pandas as pd


def best_record_company():
    top40_df = pd.read_csv("UK-top40-1964-1-2.tsv", sep="\t")
    print(top40_df.to_string())

    publisher_gr = top40_df.groupby("Publisher")
    print(publisher_gr)

    sum_records = publisher_gr["WoC"].sum()
    pub_name = sum_records.nlargest(1).index

    return top40_df[top40_df["Publisher"] == pub_name.values[0]]


def main():
    brc = best_record_company()
    print(brc)

if __name__ == "__main__":
    main()
