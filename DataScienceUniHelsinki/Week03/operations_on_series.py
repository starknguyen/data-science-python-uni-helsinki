#!/usr/bin/env python3

import pandas as pd


def create_series(L1, L2):
    return pd.Series(L1, index=["a", "b", "c"]), pd.Series(L2, index=["a", "b", "c"])


def modify_series(s1, s2):
    new_idx = pd.Index(["d"])
    s1.index.append(new_idx)
    s1["d"] = s2["b"]
    del s2["b"]
    return s1, s2


def main():
    L1 = [2, 3, 4]
    L2 = [9, 8, 7]
    s1, s2 = create_series(L1, L2)
    s1, s2 = modify_series(s1, s2)
    print(f"s1={s1}\ns2={s2}")
    sum_s = s1 + s2
    print(f"sum_s=\n{sum_s}")


if __name__ == "__main__":
    main()
