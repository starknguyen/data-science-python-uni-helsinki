#!/usr/bin/env python3

import sys
import math
import unittest
from unittest.mock import patch
from Week02.exercise05.src.summary import summary


class Summary(unittest.TestCase):

    def test_one(self):
        s,a,d = summary("src/example.txt")
        self.assertAlmostEqual(s, 51.400000, places=4, msg="Wrong sum for file example.txt!")
        self.assertAlmostEqual(a, 10.280000, places=4, msg="Wrong average for file example.txt!")
        self.assertAlmostEqual(d, 8.904606, places=4, msg="Wrong std for file example.txt!")

    def test_two(self):
        s,a,d = summary("src/example2.txt")
        self.assertAlmostEqual(s, 5446.200000, places=4, msg="Wrong sum for file example2.txt!")
        self.assertAlmostEqual(a, 1815.400000, places=4, msg="Wrong average for file example2.txt!")
        self.assertAlmostEqual(d, 3124.294045, places=4, msg="Wrong std for file example2.txt!")

    def test_three(self):
        s,a,d = summary("src/example3.txt")
        self.assertAlmostEqual(s, 0.000000, places=4, msg="Wrong sum for file example3.txt!")
        self.assertAlmostEqual(a, 0.000000, places=4, msg="Wrong average for file example3.txt!")
        self.assertAlmostEqual(d, 50.000000, places=4, msg="Wrong std for file example3.txt!")

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            summary("doesnotexist")

    def test_calls(self):
        with patch('builtins.open', side_effect=open) as o:
            summary("src/example.txt")
            o.assert_called()

    def test_main(self):
        orig_argv = sys.argv
        n = 7
        sys.argv[1:] = ["file%i" % i for i in range(n)]
        with patch('src.summary.summary',
                   side_effect=[(0.0,0.0,0.0)]*n) as s:
            summary().main()
            self.assertEqual(s.call_count, n,
                             msg="Expected %i calls to summary for %i command line parameters!" % (n,n))
        result = sys.stdout.split('\n')
        for i, line in enumerate(result):
            self.assertEqual(line.strip(), "File: file%i Sum: 0.000000 Average: 0.000000 Stddev: 0.000000" % i,
                             msg="Wrong output from main function for seven files containing only zeros!")
        sys.argv = orig_argv


if __name__ == '__main__':
    unittest.main()

