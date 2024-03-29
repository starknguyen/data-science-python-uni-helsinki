#!/usr/bin/env python3

import unittest
from unittest.mock import patch

import numpy as np
from Week02.vector_angles import vector_angles

module_name = "vector_angles"


class VectorAngles(unittest.TestCase):

    def test_first(self):
        A = np.array([[0, 0, 1], [-1, 1, 0]])
        B = np.array([[0, 1, 0], [1, 1, 0]])
        a = vector_angles(A, B)
        np.testing.assert_allclose(a, [90, 90],

                                   err_msg="Incorrect result for vectors %s and %s!" % (A, B))
    """
    def test_main(self):
        with patch(ph("vector_angles"), wraps=vector_angles) as va:
            main()
        self.assertGreaterEqual(va.call_count, 1,
                                msg="You should call the vector_angles function from the main function!")
    """

    def test_zero(self):
        n = 10
        A = np.random.randn(n, 3)
        a = vector_angles(A, A)
        np.testing.assert_allclose(a, [0] * 10, atol=1e-04,
                                   err_msg="Incorrect result for vectors %s and %s!" % (A, A))


if __name__ == '__main__':
    unittest.main()

