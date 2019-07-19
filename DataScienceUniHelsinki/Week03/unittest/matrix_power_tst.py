#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import functools
from Week03.matrix_power import matrix_power


class MatrixPower(unittest.TestCase):

    def test_one(self):
        a = np.array([[1,2], [3,4]])
        np.testing.assert_array_equal(a, matrix_power(a, 1),
                                      err_msg="Raising to power one should not change the matrix!")

    def test_zero(self):
        a = np.array([[1,2], [3,4]])
        np.testing.assert_array_equal(np.eye(2), matrix_power(a, 0),
                                      err_msg="Raising to power 0 should produce identity matrix!")

    def test_multiply(self):
        a = np.array([[1,2], [3,4]])
        for i in range(1,4):
            a1 = matrix_power(a, i)
            a2 = matrix_power(a, -i)
            np.testing.assert_array_almost_equal(np.eye(2), a1@a2,
                                                 err_msg="Multiplying a matrix and its inverse should produce identity matrix! "
                                                 "Input was matrix_power(a, %i) @ matrix_power(a, -%i), where a=\n%s" %(i,i,a))

    def test_exponents(self):
        a = np.array([[1,2], [3,4]])
        np.testing.assert_array_almost_equal(matrix_power(a, 2), a@a, err_msg="Incorrect power of 2 for matrix\n%s!" % a)
        np.testing.assert_array_almost_equal(matrix_power(a, 3), a@a@a, err_msg="Incorrect power of 3 for matrix\n%s!" % a)
        np.testing.assert_array_almost_equal(matrix_power(a, 4), a@a@a@a, err_msg="Incorrect power of 4 for matrix\n%s!" % a)

    """
    def test_called(self):
        a = np.array([[1,2], [3,4]])
        with patch(ph("functools.reduce"), wraps=functools.reduce) as preduce:
            p = matrix_power(a, -2)
            preduce.assert_called()
    """


if __name__ == '__main__':
    unittest.main()

