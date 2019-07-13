#!/usr/bin/env python3
def transform(s1, s2):
    return [i[0] * i[1] for i in zip(list(map(int, s1.split())), list(map(int, s2.split())))]


def main():
    l1 = "1 5 3"
    l2 = "2 6 -1"
    print(transform(l1, l2))


if __name__ == "__main__":
    main()
