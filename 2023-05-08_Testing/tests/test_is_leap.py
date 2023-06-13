import unittest
from main import is_leap


class TestIsLeap(unittest.TestCase):
    def test_returns_true_when_leap_year(self):
        result = is_leap(2000)
        self.assertTrue(result)

    def test_returns_falsa_when_not_leap_year(self):
        result = is_leap(2001)
        self.assertFalse(result)

    # def test_raises_error_whenstr_is_passed(self):
    #     with self.assertRaises(TypeError):
    #         is_leap("labas")