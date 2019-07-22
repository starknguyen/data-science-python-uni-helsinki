#!/usr/bin/env python3

import pandas as pd


def main():
    data = pd.read_csv("municipal.tsv", sep='\t')
    print(f"Shape: {data.shape[0]},{data.shape[1]}")
    print("Columns:")
    for col in data.columns:
        print(col)


if __name__ == "__main__":
    main()
