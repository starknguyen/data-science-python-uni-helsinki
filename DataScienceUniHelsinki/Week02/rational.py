#!/usr/bin/env python3


class Rational(object):
    """
    Represent rational number
    """
    def __init__(self, numerator, denominator):
        """
        Construct the rational number from its components
        :param numerator:
        :param denominator:
        """
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        numerator = self.numerator * other.denominator + \
                         self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - \
                         self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Rational(numerator, denominator)

    def __eq__(self, other):
        val = self - other
        if val.numerator == 0:
            return True
        else:
            return False

    def __gt__(self, other):
        val = self - other
        if val.numerator > 0:
            return True
        else:
            return False

    def __lt__(self, other):
        val = self - other
        if val.numerator < 0:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))


if __name__ == "__main__":
    main()
