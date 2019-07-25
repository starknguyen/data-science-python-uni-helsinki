#!/usr/bin/env python3

import pandas as pd


def suicide_fractions():
    df = pd.read_csv("who_suicide_statistics.csv")

    df["avg"] = df["suicides_no"] / df["population"]
    gr = df.groupby("country")["avg"].mean()

    return gr


def suicide_weather():
    dat_temp = pd.read_html("List_of_countries_by_average_yearly_temperature.html", index_col="Country")[0]
    #print(dat_temp.dtypes)

    dat_temp["Average yearly temperature (1961–1990, degrees Celsius)"] = \
        dat_temp["Average yearly temperature (1961–1990, degrees Celsius)"].str.replace("\u2212", "-")

    dat_temp["Average yearly temperature (1961–1990, degrees Celsius)"] = \
        dat_temp["Average yearly temperature (1961–1990, degrees Celsius)"].astype(float)
    # print(len(dat_temp))

    suicide_frac = suicide_fractions()
    # print(len(suicide_frac))

    df = dat_temp.join(suicide_frac, how="inner")
    # print(df)

    spearman_corr = suicide_frac.corr(dat_temp["Average yearly temperature (1961–1990, degrees Celsius)"],
                                             method="spearman")
    print(spearman_corr)

    return len(suicide_frac), len(dat_temp), len(df), spearman_corr


def main():
    sw = suicide_weather()
    print(f"Suicide DataFrame has {sw[0]} rows")
    print(f"Temperature DataFrame has {sw[1]} rows")
    print(f"Common DataFrame has {sw[2]} rows")
    print((f"Spearman correlation: {sw[3]}"))


if __name__ == "__main__":
    main()
