#!/usr/bin/env python3

import pandas as pd


def cities():
    population_ser = pd.Series([643272, 279044, 231853, 223027, 201810])
    area_ser = pd.Series([715.48, 528.03, 689.59, 240.35, 3817.52])
    city_ser = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]

    df =  pd.DataFrame({"Population": population_ser, "Total area": area_ser})
    df.index = city_ser
    return df


def main():
    print(cities())


if __name__ == "__main__":
    main()
