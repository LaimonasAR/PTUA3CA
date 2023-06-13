import unittest
import calculator

class CalculatorTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.add(2, -2), 0)
        self.assertEqual(calculator.add(10, 100), 110)
    def test_subtraction(self):
        self.assertEqual(calculator.subtract(2, 2), 0)
        self.assertEqual(calculator.subtract(0, 2), -2)
    def test_multiplication(self):
        self.assertEqual(calculator.multiply(2, 2), 4)
    def test_division(self):
        self.assertEqual(calculator.divide(2, 2), 1)
        self.assertRaises(ZeroDivisionError, calculator.divide, 1, 0)