import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(calculator.square_root(9), 3)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-4)

if __name__ == '__main__':
    unittest.main()
