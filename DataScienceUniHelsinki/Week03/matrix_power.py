#!/usr/bin/env python3

import numpy as np
import functools


def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0])
    elif n > 0:
        return functools.reduce(np.matmul, (a for __ in range(0, n)))
    elif n < -1:
        return functools.reduce(np.matmul, (np.linalg.inv(a) for __ in range(0, -n)))


def main():
    a = np.array([[1, 6, 7],
                  [7, 8, 1],
                  [5, 9, 8]])

    n = -2
    print(matrix_power(a, n))


if __name__ == "__main__":
    main()
