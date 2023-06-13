import unittest

from main import Roman

class UnitTests(unittest.TestCase):

    def setUp(self) -> None:
        self.roman = Roman()

    def test_roman_number_conversion_five(self):
        self.assertEqual(self.roman.convert(5), "V")

    def test_roman_number_conversion_nine(self):
        self.assertEqual(self.roman.convert(9), "IX")

    def test_roman_number_conversion_forty(self):
        self.assertEqual(self.roman.convert(40), "XL")

    def test_roman_number_conversion_nineteen_o_four(self):
        self.assertEqual(self.roman.convert(1904), "MCMIV")
    
    

# Input: 5
# Output: V

# Input: 9
# Output: IX

# Input: 40
# Output: XL

# Input: 1904
# Output: MCMIV