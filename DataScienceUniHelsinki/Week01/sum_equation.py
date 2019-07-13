#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        return "0 = 0"

    lhs = " + ".join("%s" % val for val in L).rstrip(" ")
    rhs = sum(val for val in L)

    return lhs + " = " + str(rhs)

def main():
    li = [1, 5, 7]
    print(sum_equation(li))

if __name__ == "__main__":
    main()
