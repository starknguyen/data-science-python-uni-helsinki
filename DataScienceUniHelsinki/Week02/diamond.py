#!/usr/bin/env python3

import numpy as np


def diamond(n):
    # n must be an odd
    n = 2*n - 1
    half_rows = int(n / 2) + 1
    d = np.eye(half_rows, n, dtype=int)
    d[0, 0] = 0
    d[0, half_rows - 1] = 1
    r = 1
    while r < half_rows:
        d[r, r] = 0
        d[r, int(n / 2) + r] = 1
        d[r, int(n / 2) - r] = 1
        r += 1

    d = np.concatenate((d[0: half_rows - 1], d[::-1]))

    return d


def main():
    print(diamond(3))


if __name__ == "__main__":
    main()
