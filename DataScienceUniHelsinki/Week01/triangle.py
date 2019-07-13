"""
Right-angled triangle module
"""

__author__ = "Nghi Dinh Nguyen"
__version__ = "0.1.0"

import math

def hypothenuse(side_a, side_b):
    """
    Calculate hypothenuse length of a right-angled triangle
    :return: hypothenuse length
    """
    return math.sqrt(side_a**2 + side_b**2)


def area(side_a, side_b):
    """
    Calculate area of a right-angled triangle
    :return: area value
    """
    return side_a * side_b / 2