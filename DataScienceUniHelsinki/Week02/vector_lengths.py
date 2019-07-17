#!/usr/bin/env python3

import numpy as np


def vector_lengths(a):
    return np.sqrt(np.sum(a**2, axis=1))


def main():
    arr = np.random.randint(1, 10, (4, 5))
    print(vector_lengths(arr))


if __name__ == "__main__":
    main()
