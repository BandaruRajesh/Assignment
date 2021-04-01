"""
"""
"""
Given an integer n, return the minimum number you can make by inserting 3 anywhere in the number.

Example 1
Input
n = 526
Output
3526

Example 2
Input
n = 235
Output
2353
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def MinNUm(n):
    pass

# DO NOT TOUCH THE BELOW CODE
class TestMinNum(unittest.TestCase):

    def test_01(self):
        self.assertEqual(MinNum(526), 3526)

    def test_02(self):
        self.assertEqual(MinNum(235), 2353)

    


if __name__ == '__main__':
    unittest.main(verbosity=2)
