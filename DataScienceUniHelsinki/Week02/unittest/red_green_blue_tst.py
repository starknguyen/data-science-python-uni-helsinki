#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from Week02.red_green_blue import red_green_blue


class RedGreenBlue(unittest.TestCase):

    def test_size(self):
        result = red_green_blue()

        self.assertEqual(len(result), 753, "Wrong number of strings in the returned list!")
        for s in result:
            self.assertEqual(len(s.split("\t")), 4, msg="String %s does not have four fields separated by a tab!")

    def test_content(self):
        result = red_green_blue()
        for i, s in enumerate(result):
            pos = "in result list with index %i: %s" % (i, s)
            t = s.split("\t")
            r = int(t[0])
            g = int(t[1])
            b = int(t[2])
            name = t[3]
            self.assertGreaterEqual(r, 0, msg="The value of the red component should be in the range [0,255] %s!" % pos)
            self.assertLessEqual(r, 255, msg="The value of the red component should be in the range [0,255] %s!" % pos)
            self.assertGreaterEqual(g, 0,
                                    msg="The value of the green component should be in the range [0,255] %s!" % pos)
            self.assertLessEqual(g, 255,
                                 msg="The value of the green component should be in the range [0,255] %s!" % pos)
            self.assertGreaterEqual(b, 0,
                                    msg="The value of the blue component should be in the range [0,255] %s!" % pos)
            self.assertLessEqual(b, 255, msg="The value of the blue component should be in the range [0,255] %s!" % pos)
        t = result[1].split("\t")
        r = int(t[0])
        g = int(t[1])
        b = int(t[2])
        name = t[3]

        self.assertEqual(r, 248, msg="Incorrect value of red component in the second string!")
        self.assertEqual(g, 248, msg="Incorrect value of green component in the second string!")
        self.assertEqual(b, 255, msg="Incorrect value of blue component in the second string!")
        self.assertEqual(name, "ghost white", msg="Incorrect color name in the second string!")
    """
    def test_called(self):
        with patch('builtins.open', side_effect=open) as o, \
                patch(ph('re.match'), side_effect=re.match) as m, \
                patch(ph('re.fullmatch'), side_effect=re.fullmatch) as fm, \
                patch(ph('re.search'), side_effect=re.search) as s, \
                patch(ph('re.findall'), side_effect=re.findall) as fa, \
                patch(ph('re.finditer'), side_effect=re.finditer) as fi:
            result = red_green_blue()
            o.assert_called()
            self.assertTrue(m.called or fm.called or s.called or fa.called or fi.called,
                            msg="Expected that either re.match, re.fullmatch, re.search, re.findall, re.finditer is called!")
    """


if __name__ == '__main__':
    unittest.main()

