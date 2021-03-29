"""
Given an integer n, return whether its prime factors only include 2, 3 or 5.

Constraints

0 ≤ n < 2 ** 31
Example 1
Input
n = 10
Output
True
Explanation
10's prime factors are 2 and 5.
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def solve(n):
    pass

# DO NOT TOUCH THE BELOW CODE
class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(solve(134), False)

    def test_02(self):
        self.assertEqual(solve(160), True)

    def test_03(self):
        self.assertEqual(solve(982941), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)


