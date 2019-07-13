#!/usr/bin/env python3

def positive_list(L):
    return list(filter(lambda x: x > 0, L))


def main():
    l = [2,-2,0,1,-7]
    print(positive_list(l))

if __name__ == "__main__":
    main()
