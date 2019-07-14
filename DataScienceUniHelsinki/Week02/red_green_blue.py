#!/usr/bin/env python3

import re


def red_green_blue(filename="rgb.txt"):
    with open(filename, 'r') as f:
        lines = f.readlines()
    retval = []
    for line in lines[1:]:
        print(line)
        # Find numbers
        nums = re.findall(r"\b(\d+)\s*", line)
        if not len(nums) == 3:
            raise Exception('Expected to receive 3 numbers here')
        # Find color name
        s = re.findall(r"\s*(\w+[\w|\s]\w+)", line)
        retval.append("{}\t{}\t{}\t{}".format(nums[0], nums[1], nums[2], s[-1]))

    return retval


def main():
    print(red_green_blue())


if __name__ == "__main__":
    main()
