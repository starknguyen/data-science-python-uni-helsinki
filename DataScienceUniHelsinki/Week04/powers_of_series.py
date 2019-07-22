#!/usr/bin/env python3

import pandas as pd


def powers_of_series(s, k):
    s.name = 1
    cols = [s]
    for i in range(2, k + 1):
        ser = pd.Series(s.values ** i, name=i, index=s.index)
        cols.append(ser)

    df = pd.concat(cols, axis=1, keys=[s.name for s in cols])
    return df


def main():
    s = pd.Series([1, 2, 3, 4], index=list("abcd"))
    print(powers_of_series(s, 4))


if __name__ == "__main__":
    main()
