#!/usr/bin/env python3


class Prepend(object):
    # Add the methods of the class here
    def __init__(self, in_str):
        self.start = in_str

    def write(self, s):
        print(self.start + s)


def main():
    prepend = Prepend("+++ ")
    prepend.write("Hello")


if __name__ == "__main__":
    main()
