#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from Week01.find_matching import find_matching


class FindMatching(unittest.TestCase):

    def test_first(self):
        result = find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
        self.assertEqual(result, [0,1,3])

    def test_calls(self):
        with patch('builtins.enumerate') as p:
            result = find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
            p.assert_called()

    def test_empty(self):
        result = find_matching([], "en")
        self.assertEqual(result, [], msg="Empty list cannot contain any matches!")


if __name__ == '__main__':
    unittest.main()

