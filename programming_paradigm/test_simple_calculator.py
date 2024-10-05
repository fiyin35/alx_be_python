import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)  # add assertion here
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(10, -1), 11)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)
        self.assertEqual(self.calc.multiply(10, 5), 50)
    def test_division(self):
        self.assertEqual(self.calc.divide(5, 5), 1)
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(5, 0), None)


if __name__ == '__main__':
    unittest.main()
