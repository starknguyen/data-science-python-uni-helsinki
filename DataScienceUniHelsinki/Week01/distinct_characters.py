#!/usr/bin/env python3
def distinct_characters(L):
    retval = {}
    for str in L:
        retval[str] = len(set(str))
    return retval


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
