#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from Week02.word_frequencies import word_frequencies


class WordFrequencies(unittest.TestCase):

    def test_first(self):
        d = word_frequencies("/home/nguydin/PycharmProjects/data-science-python-uni-helsinki/DataScienceUniHelsinki/Week02/alice.txt")
        self.assertEqual(d['creating'], 3, msg="Incorrect count for word 'creating'!")
        self.assertEqual(d['Carroll'], 3, msg="Incorrect count for word 'Carroll'!")
        self.assertEqual(d['sleepy'], 2, msg="Incorrect count for word 'sleepy'!")
        self.assertEqual(d['Rabbit'], 28, msg="Incorrect count for word 'Rabbit'!")

        self.assertEqual(len(d), 2424, msg="Wrong number of words in the dictionary!")

    def test_calls(self):
        with patch('builtins.open', wraps=open) as o:
            d = word_frequencies("/home/nguydin/PycharmProjects/data-science-python-uni-helsinki/DataScienceUniHelsinki/Week02/alice.txt")
            o.assert_called()


if __name__ == '__main__':
    unittest.main()

