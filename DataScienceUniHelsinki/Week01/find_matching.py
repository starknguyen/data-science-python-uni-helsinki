#!/usr/bin/env python3

def find_matching(L, pattern):
    return [i[0] for i in list(enumerate(L)) if pattern in i[1]]

def main():
    pass

if __name__ == "__main__":
    main()
