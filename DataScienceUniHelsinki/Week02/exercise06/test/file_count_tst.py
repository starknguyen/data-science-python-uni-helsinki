#!/usr/bin/env python3

import sys
import unittest
from unittest.mock import patch
from Week02.exercise06.src.file_count import file_count


class FileCount(unittest.TestCase):

    def test_first(self):
        l, w, c = file_count("src/test.txt")
        self.assertEqual(l, 8, msg="Wrong number of lines for file 'test.txt'!")
        self.assertEqual(w, 105, msg="Wrong number of words for file 'test.txt'!")
        self.assertEqual(c, 647, msg="Wrong number of characters for file 'test.txt'!")

    def test_calls(self):
        with patch('builtins.open', side_effect=open) as o:
            file_count("src/test.txt")
            o.assert_called_once()

    def test_main(self):
        orig_argv = sys.argv
        n = 7
        sys.argv[1:] = ["file%i" % i for i in range(n)]
        with patch('src.file_count.file_count', side_effect=[(0,0,0)]*n) as fc:
            file_count.main()
            self.assertEqual(fc.call_count, n,
                             msg="Wrong number of calls to function 'file_count' for %i command line parameters!" % n)
        result = sys.stdout().split('\n')
        for i, line in enumerate(result):
            self.assertEqual(line.strip(), "0\t0\t0\tfile%i" % i,
                             msg="Wrong result on line %i!" % i)
        sys.argv = orig_argv


if __name__ == '__main__':
    unittest.main()

