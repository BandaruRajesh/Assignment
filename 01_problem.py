"""
Given a positive integer n, determine whether you can make n by summing up some non-negative multiple of 3 and some non-negative multiple of 7.

Constraints

n < 2 ** 31
Example 1
Input
n = 13
Output
True
Explanation
We can get 13 with 1 * 7 + 2 * 3."""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def solve(n):
    pass


# DO NOT TOUCH THE BELOW CODE
class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(solve(24),True)

    def test_02(self):
        self.assertEqual(solve(95746), True)

    def test_03(self):
        self.assertEqual(solve(1), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)

