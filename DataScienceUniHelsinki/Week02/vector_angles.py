#!/usr/bin/env python3

import numpy as np


def vector_angles(X, Y):
    if (X == Y).all():
        return np.zeros(X.shape[0])
    n = np.inner(X, Y)
    d = np.sqrt(np.sum(X**2)) * np.sqrt(np.sum(Y**2))
    r = np.arccos(np.clip(n / d, -1.0, 1.0))
    return np.degrees(r)[0]


def main():
    #x = np.array([2, 2])
    #y = np.array([0, 3])
    #A = np.array([[0, 0, 1], [-1, 1, 0]])
    #B = np.array([[0, 1, 0], [1, 1, 0]])
    #print(vector_angles(A, B))

    #n = 10
    #A = np.random.randn(n, 3)
    #print(vector_angles(A, A))

    x = np.array([[2, 2], [1, 2]])
    y = np.array([[0, 3], [1, 3]])
    print(vector_angles(x, y))


if __name__ == "__main__":
    main()
