from simple_calculator import SimpleCalculator
import unittest
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_subtraction(self):        
        self.assertEqual(self.calc.subtract(3,2), 3)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4,5),3)
    def test_division(self):
        self.asserEqual(self.calc.divide(9,7),8)
