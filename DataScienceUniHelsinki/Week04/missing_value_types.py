#!/usr/bin/env python3

import pandas as pd
import numpy as np


def missing_value_types():
    states = pd.Series(["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"])
    year_dep = pd.Series([np.nan, 1917, 1776, 1523, np.nan, 1992])
    presidents = pd.Series([None, "Niinistö", "Trump", None, "Steinmeier", "Putin"])
    return pd.DataFrame({"State": states, "Year of independence": year_dep, "President": presidents}).set_index("State")


def main():
    df = missing_value_types()
    print(df)


if __name__ == "__main__":
    main()
