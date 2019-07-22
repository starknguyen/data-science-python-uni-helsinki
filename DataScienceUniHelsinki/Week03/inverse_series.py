#!/usr/bin/env python3

import pandas as pd


def inverse_series(s):
    return pd.Series(s.index.values, index=s)


def main():
    s = pd.Series([1, 2, 3, 4], index=list("abcd"))
    print(s)
    inv_s = inverse_series(s)
    print(inv_s)


if __name__ == "__main__":
    main()
