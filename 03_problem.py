"""
Given an integer n, return whether n = k * k for some integer k.

This should be done without using built-in square root function.

Constraints

0 ≤ n < 2 ** 31
Example 1
Input
n = 25
Output
True
Explanation
25 = 5 * 5

"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def solve(n):
    pass

# DO NOT TOUCH THE BELOW CODE
class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(solve(425), False)

    def test_02(self):
        self.assertEqual(solve(45369), True)

    def test_03(self):
        self.assertEqual(solve(1342563), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)


