import unittest
import buggy_calculator as calc

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(5, 3), 8)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(0, 0), 0)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 4), 6)
        self.assertEqual(calc.subtract(5, 10), -5)
        self.assertEqual(calc.subtract(0, 0), 0)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(6, 7), 42)
        self.assertEqual(calc.multiply(-2, 3), -6)
        self.assertEqual(calc.multiply(0, 5), 0)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(10, 0), "Ошибка: деление на ноль!")
        self.assertEqual(calc.divide(0, 5), 0)
    
    def test_power(self):
        self.assertEqual(calc.power(2, 3), 8)
        self.assertEqual(calc.power(5, 0), 1)
        self.assertEqual(calc.power(2, -1), 0.5)
    
    def test_mod(self):
        self.assertEqual(calc.mod(10, 3), 1)
        self.assertEqual(calc.mod(10, 0), "Ошибка: деление на ноль!")
        self.assertEqual(calc.mod(5, 2), 1)

if __name__ == '__main__':
    unittest.main()
