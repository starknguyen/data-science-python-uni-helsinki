#!/usr/bin/env python3

import numpy as np


def most_frequent_first(a, c):
    retval = []
    # Get array with frequency of elements in column
    mfrq_arr = np.array(np.unique(a[:, c], return_counts=True)).T
    # Sort by frequencies
    mfrq_arr = mfrq_arr[np.argsort(mfrq_arr[:, 1])][::-1]

    for i in mfrq_arr[:, 0]:
        retval.append(a[a[:, c] == i])

    return np.concatenate(retval)


def main():
    a = np.array([[1, 2, 3, 4, 5, 9], [2, 0, 0, 0, 0, 8], [3, 0, 0, 0, 0, 4], [4, 0, 0, 0, 0, 9], [3, 4, 0, 0, 0, 1],
                  [8, 3, 0, 0, 0, 3], [6, 6, 0, 0, 0, 3], [1, 2, 0, 0, 0, 1], [2, 5, 0, 0, 0, 3]])

    print(most_frequent_first(a, -1))


if __name__ == "__main__":
    main()
