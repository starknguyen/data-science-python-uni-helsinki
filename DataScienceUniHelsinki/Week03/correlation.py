#!/usr/bin/env python3

import scipy.stats
import numpy as np


def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "Week03", filename)


def load2():
    """This loads the data from the internet. Does not work well on the TMC server."""
    import seaborn as sns
    return sns.load_dataset('iris').drop('species', axis=1).values


def load():
    import pandas as pd
    return pd.read_csv(get_path("iris.csv")).drop('species', axis=1).values
    # return pd.read_csv("src/iris.csv").drop('species', axis=1).values


def lengths():
    data = load()
    return scipy.stats.pearsonr(data[:, 0], data[:, 2])[0]


def correlations():
    data = load()
    return np.corrcoef(data.T)


def main():
    print(lengths())
    print(correlations())


if __name__ == "__main__":
    main()
