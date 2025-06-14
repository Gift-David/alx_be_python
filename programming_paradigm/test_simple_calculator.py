
import unittest
from simple_calculator import SimpleCalculator

def SimpleCalculator():
    pass
class Test(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(SimpleCalculator.add(self, 5,5), 10)
        self.assertEqual(self.calc.add)

    def test_subtraction(self):
        self.assertEqual(SimpleCalculator.subtract(self, 10,5), 5)

    def test_multiplication(self):
        self.assertEqual(SimpleCalculator.multiply(self, 10,5), 50)

    def test_division(self):
        self.assertEqual(SimpleCalculator.divide(self, 20,5), 4)
        self.assertEqual(SimpleCalculator.divide(self, 20,0), ZeroDivisionError())