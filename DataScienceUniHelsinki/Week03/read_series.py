#!/usr/bin/env python3

import pandas as pd
import re


def read_series():
    indices = []
    values = []

    while True:
        usr_input = input("Enter series input: ")
        if usr_input == "":
            break
        # Validate input
        if ' ' not in usr_input and '\t' not in usr_input:
            raise Exception("Input must have space separated")

        indices.append(re.findall(r"^\w", usr_input)[0])
        values.append(re.findall(r"\b\s+\w+", usr_input)[0].strip())

    print(f"incides = {indices}")
    print(f"values = {values}")

    # Create series
    sr = pd.Series(values, index=indices)
    return sr


def main():
    print(read_series())


if __name__ == "__main__":
    main()
