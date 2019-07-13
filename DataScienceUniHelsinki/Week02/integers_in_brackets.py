#!/usr/bin/env python3

import re


def integers_in_brackets(s):
    a = re.findall(r'\[(.*?)\]', s)
    return [int(i.replace("+", "")) for i in a if re.match(r'[\t+-]|\d+.*(?<!\+)$', i)]

def main():
    pass

if __name__ == "__main__":
    main()
