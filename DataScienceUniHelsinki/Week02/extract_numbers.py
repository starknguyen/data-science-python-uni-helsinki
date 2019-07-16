#!/usr/bin/env python3


def extract_numbers(s):
    comps = s.split(" ")
    retval = []
    if len(comps) == 0:
        return None
    for comp in comps:
        try:
            retval.append(int(comp))
        except ValueError:
            try:
                retval.append(float(comp))
            except ValueError:
                continue
    return retval


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))


if __name__ == "__main__":
    main()
