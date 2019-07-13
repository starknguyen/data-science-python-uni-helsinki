#!/usr/bin/env python3

def interleave(*lists):
    z = zip(*lists)
    retval = []
    for tup in z:
        for l in tup:
            retval.append(l)

    return retval


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
