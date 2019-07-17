#!/usr/bin/env python3

import numpy as np


def get_rows(a):
    rows = []
    for row_idx in range(0, a.shape[0]):
        rows.append(a[row_idx, :])
    return rows


def get_columns(a):
    cols = []
    b = a.T
    for col_idx in range(0, b.shape[0]):
        cols.append(b[col_idx, :])
    return cols


def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))


if __name__ == "__main__":
    main()
