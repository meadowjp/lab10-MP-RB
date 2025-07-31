#https://github.com/meadowjp/lab10-MP-RB

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

    if __name__ == '__main__':
        unittest.main()

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mult(2,3), 6)
        self.assertEqual(mult(3,5), 15)
        self.assertEqual(mult(-1,3), -3)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,4),2)
        self.assertEqual(div(-3,9),-3)
        self.assertEqual(div(2,6),3)
    

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
              log(5,0)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
    
    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-1)
    #     # Test basic function
    #     fill in code
    

# Do not touch this
if __name__ == "__main__":
    unittest.main()
