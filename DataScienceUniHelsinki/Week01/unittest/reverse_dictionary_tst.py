#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from Week01.reverse_dictionary import reverse_dictionary


class ReverseDictionary(unittest.TestCase):

    def test_first(self):
        d = {"move": ["liikuttaa"], "hide": ["piilottaa", "salata"]}
        sd = str(d)
        r = reverse_dictionary(d)
        self.assertEqual(r["liikuttaa"], ["move"], msg="Incorrect translation of 'liikuttaa' for dict %s!" % sd)
        self.assertEqual(r["piilottaa"], ["hide"], msg="Incorrect translation of 'piilottaa' for dict %s!" % sd)
        self.assertEqual(r["salata"], ["hide"], msg="Incorrect translation of 'salata' for dict %s!" % sd)
        self.assertEqual(len(r), 3, msg="Incorrect number of elements in result for dict %s!" % d)

    def test_second(self):
        d = {"move": ["liikuttaa"], "hide": ["piilottaa", "salata"], "six": ["kuusi"], "fir": ["kuusi"]}
        sd = str(d)
        r = reverse_dictionary(d)
        self.assertEqual(r["liikuttaa"], ["move"], msg="Incorrect translation of 'liikuttaa' for dict %s!" % sd)
        self.assertEqual(r["piilottaa"], ["hide"], msg="Incorrect translation of 'piilottaa' for dict %s!" % sd)
        self.assertEqual(r["salata"], ["hide"], msg="Incorrect translation of 'salata' for dict %s!" % sd)
        self.assertEqual(set(r["kuusi"]), set(["fir", "six"]), msg="Incorrect translation of 'kuusi' for dict %s!" % sd)
        self.assertEqual(len(r), 4, msg="Incorrect number of elements in result for dict %s!" % d)


if __name__ == '__main__':
    unittest.main()

