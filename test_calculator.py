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
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(-1, -1), 0)
        self.assertEqual(sub(0, 5), -5)

    def test_multiply(self): 
        self.assertEqual(mult(2,3), 6)
        self.assertEqual(mult(3,5), 15)
        self.assertEqual(mult(-1,3), -3)

    def test_divide(self): 
        self.assertEqual(div(2,4),2)
        self.assertEqual(div(-3,9),-3)
        self.assertEqual(div(2,6),3)

    def test_divide_by_zero(self):
        self.assertEqual(div(5, 0), "Division error")

    def test_logarithm(self):
        self.assertAlmostEqual(log(8, 2), 3.0)
        self.assertAlmostEqual(log(100, 10), 2.0)
        self.assertAlmostEqual(log(math.e, math.e), 1.0)

    def test_log_invalid_base(self):
        self.assertEqual(log(-5, 2), "Value error")

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
              log(5,0)
    
    def test_hypotenuse(self): 
        with self.assertEqual(hypotenuse(3,4),5)
        with self.assertEqaul(hypotenuse(5,12),13)
        with self.assertEqual(hypotenuse(8,15),17)
    
    def test_sqrt(self): 
        with self.assertRaises(ValueError):
            square_root(-1)
 

if __name__ == "__main__":
    unittest.main()
