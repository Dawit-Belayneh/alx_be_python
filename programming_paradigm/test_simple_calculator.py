import unittest
from simple_calculator import SimpleCalculator

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = SimpleCalculator.add(self, 5, 2)
        self.assertEqual(result, 7)
    
    def test_sub(self):
       result = SimpleCalculator.subtract(self, 5, 2)
       self.assertEqual(result, 3)
    
    def test_divide(self):
        result = SimpleCalculator.divide(self, 10, 2)
        self.assertEqual(result, 5)
    
    def test_product(self):
        result = SimpleCalculator.multiply(self, 10, 2)
        self.assertEqual(result, 20)


if __name__ == "__main__":
    unittest.main()
