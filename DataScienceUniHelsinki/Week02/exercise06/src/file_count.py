#!/usr/bin/env python3

import sys

def file_count(filename):
    n_words = 0
    n_chars = 0
    with open(filename, 'r') as f:
        content = f.read()
        n_chars = len(content)
        lines = content.split("\n")
        n_lines = len(lines)
        if lines[-1] == "":
            n_lines -= 1
        for line in lines:
            line = line.strip("\n")
            words = line.split()
            n_words += len(words)

    return n_lines, n_words, n_chars


def main():
    print(file_count("/home/nguydin/PycharmProjects/data-science-python-uni-helsinki/DataScienceUniHelsinki/Week02/exercise06/src/test.txt"))


if __name__ == "__main__":
    main()
