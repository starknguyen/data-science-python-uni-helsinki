#!/usr/bin/env python3

import re


def file_listing(filename="listing.txt"):
    retval = []
    with open(filename, 'r') as f:
        for line in f:
            # print(line)
            # Find "number of links", "file size", "time of last modification: day, hour, minute"
            re1 = re.findall(r"\b\s*(\d+)\s*", line)
            if not len(re1) == 5:
                raise Exception('Expected to have 5 results here')
            file_size = int(re1[1])
            file_last_mod_day = int(re1[2])
            file_last_mod_hour = int(re1[3])
            file_last_mod_min = int(re1[4])

            # Find time of last modification- month. Month str must have 3 characters
            re2 = re.findall(r"[\d+]\b\s*(\w{3}(?!\d))\s*[\d+]", line)
            if not len(re2) == 1:
                raise Exception('No string of month found')
            file_last_mod_month = re2[0]

            # Find file name and its extension
            re3 = re.findall(r"\w+[.]\w+$", line)
            if not len(re3) == 1:
                re3 = re.findall(r"\w+\w+$", line)
                if not len(re3) == 1:
                    raise Exception('No string of file name and extension found')
            file_name = re3[0]

            retval.append((file_size, file_last_mod_month, file_last_mod_day, file_last_mod_hour, file_last_mod_min, file_name))

    return retval


def main():
    print(file_listing())


if __name__ == "__main__":
    main()
