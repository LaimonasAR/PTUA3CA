import unittest
from leap import Leap

class TestLeapClass(unittest.TestCase):
    def setUp(self):
        self.leap = Leap()

    def test_check_method(self):
        self.assertFalse(self.leap.check(2100))
        self.assertTrue(self.leap.check(2000))

    def test_range_method(self):
        result = self.leap.range(1980, 2000)
        self.assertEqual(result, [1980, 1984, 1988, 1992, 1996])