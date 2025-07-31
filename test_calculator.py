#https://github.com/meadowjp/lab10-MP-RB
# Partner 1: Meadow Parks
# Partner 2: Richard Bennett

import math
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)

    def test_mul(self): 
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(3,5), 15)
        self.assertEqual(mul(-1,3), -3)

    def test_divide(self): 
        self.assertEqual(div(4,2),2)
        self.assertEqual(div(9,-3),-3)
        self.assertEqual(div(6,2),3)

    def test_divide_by_zero(self):
        self.assertEqual(div(5, 0), "Division error")

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(8, 2), 3.0)
        self.assertAlmostEqual(logarithm(100, 10), 2.0)
        self.assertAlmostEqual(logarithm(math.e, math.e), 1.0)

    def test_log_invalid_base(self):
        self.assertEqual(logarithm(-5, 2), "Value error")

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
              logarithm(5,0)
    
    def test_hypotenuse(self): 
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5,12),13)
        self.assertEqual(hypotenuse(8,15),17)
    
    def test_sqrt(self): 
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(sqrt(4),2)
        self.assertEqual(sqrt(16),4)

if __name__ == "__main__":
    unittest.main()
