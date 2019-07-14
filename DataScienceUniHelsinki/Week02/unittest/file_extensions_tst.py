#!/usr/bin/env python3

import sys
import unittest
from unittest.mock import patch
from Week02.file_extensions import file_extensions


class FileExtensions(unittest.TestCase):

    def test_first(self):
        correct_d = {'txt': ['file1.txt', 'file2.txt'],
                     'pdf': ['mydocument.pdf'],
                     'gz': ['archive.tar.gz']}
        no_extension, d = file_extensions("src/filenames.txt")
        self.assertEqual(no_extension, ["test"],
                         msg="There should be exactly one filename without an extension!")
        self.assertEqual(d, correct_d, msg="The dictionary of files with an extension is incorrect!")

    def test_calls(self):
        with patch('builtins.open', side_effect=open) as o:
            file_extensions("src/filenames.txt")
            o.assert_called_once()

    def test_main(self):
        with patch('src.file_extensions.file_extensions', side_effect=[([], {})]) as fe:
            file_extensions.main()
            self.assertEqual(fe.call_count, 1,
                             msg="You should call function 'file_extensions' from main!")
            result = sys.stdout().split('\n')
            self.assertEqual(len(result), 1, msg="Expected one line of output!")
            self.assertEqual(result[0], "0 files with no extension")


if __name__ == '__main__':
    unittest.main()

