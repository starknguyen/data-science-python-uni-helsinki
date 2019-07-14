#!/usr/bin/env python3

import sys
import math


def summary(filename):
    x = []
    with open(filename, 'r') as f:
        for w in f.read().split():
            try:
                x.append(float(w))
            except ValueError:
                continue

    s = 0
    for xi in x:
        s += xi
    avg = s / len(x)

    sq_sum = 0
    for xi in x:
        sq_sum += (xi-avg)**2

    std_dev = math.sqrt(sq_sum / (len(x)-1))

    return s, avg, std_dev


def main():
    # Format File: src/example.txt Sum: 51.400000 Average: 10.280000 Stddev: 8.904606
    for arg in sys.argv[1:]:
        s, a, d = summary(arg)
        print("File: {} Sum: {} Average: {} Stddev: {}".format(arg,
                                                               "{0:.6f}".format(s),
                                                               "{0:.6f}".format(a),
                                                               "{0:.6f}".format(d)))


if __name__ == "__main__":
    main()
