
import unittest
from simple_calculator import SimpleCalculator

class Simple_Calculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(SimpleCalculator.add(self, 5,5), 10)

    def test_subtract(self):
        self.assertEqual(SimpleCalculator.subtract(self, 10,5), 5)

    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(self, 10,5), 50)

    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(self, 20,5), 4)
        self.assertEqual(SimpleCalculator.divide(self, 20,0), ZeroDivisionError())