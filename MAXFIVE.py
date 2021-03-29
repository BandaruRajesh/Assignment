"""
Given an integer n, return the maximum number you can make by inserting 5 anywhere in the number.

Example 1
Input
n = 923
Output
9523
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def solve(n):
    pass

# DO NOT TOUCH THE BELOW CODE
class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(solve(2414135), 52414135)

    def test_02(self):
        self.assertEqual(solve(13123), 513123)

    def test_03(self):
        self.assertEqual(solve(-999999), -5999999)


if __name__ == '__main__':
    unittest.main(verbosity=2)
