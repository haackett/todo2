import unittest
from datetime import date
from datefunctions import get_distance
from datefunctions import is_to_reccur


class Tests(unittest.TestCase):

    def test_get_distance(self):
        d0 = date(2020, 11, 13)
        d1 = date(2020, 11, 20)
        self.assertEqual(get_distance(d0, d1), 7)

    def test_is_to_reccur(self):
        d0 = date(2020, 11, 13)
        d1 = date(2020, 11, 20)
        self.assertEqual(is_to_reccur(d0, d1, 7), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)