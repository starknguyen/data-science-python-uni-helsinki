#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import pandas as pd
from Week04.cyclists import cyclists


class Cyclists(unittest.TestCase):

    def test_shape(self):
        df = cyclists()
        self.assertEqual(df.shape, (37128, 21), msg="Incorrect shape!")

    def test_columns(self):
        df = cyclists()
        cols = [
            "Baana",
            "Viikintie",
            "Ratapihantie",
            "Lauttasaaren silta pohjoispuoli",
            "Pitkäsilta länsipuoli",
            "Pitkäsilta itäpuoli",
            "Heperian puisto/Ooppera",
            "Munkkiniemi silta pohjoispuoli",
            "Munkkiniemen silta eteläpuoli",
            "Merikannontie",
            "Lauttasaaren silta eteläpuoli",
            "Käpylä, Pohjoisbaana",
            "Kuusisaarentie",
            "Kulosaaren silta po. ",
            "Kulosaaren silta et.",
            "Kaivokatu",
            "Kaisaniemi/Eläintarhanlahti",
            "Huopalahti (asema)",
            "Eteläesplanadi",
            "Auroransilta",
            "Päivämäärä"]
        np.testing.assert_array_equal(df.columns, cols[::-1], err_msg="Incorrect column names!")

    """
    def test_called(self):
        method = spy_decorator(pd.core.frame.DataFrame.dropna, "dropna")
        with patch.object(pd.core.frame.DataFrame, "dropna", new=method):
            df = cyclists()
            method.mock.assert_called()
            self.assertEqual(method.mock.call_count, 2,
                             msg="Expected dropna method to be called twice!")
            for args, kwargs in method.mock.call_args_list:
                self.assertEqual(kwargs["how"], "all",
                                 msg="Expected parameter 'all' to parameter 'how'!")
    """


if __name__ == '__main__':
    unittest.main()

