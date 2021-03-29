"""
The Fibonacci sequence goes like this: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number can be found by adding up the two numbers before it, and the first two numbers are always 1.

Write a function that takes an integer n and returns the nth Fibonacci number in the sequence.

Constraints
n ≤ 30

Example 1
Input
n = 1
Output
1
Explanation
This is the base case and the first fibonacci number is defined as 1.
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def solve(n):
    pass

# DO NOT TOUCH THE BELOW CODE
class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(solve(24), 46368)

    def test_02(self):
        self.assertEqual(solve(12), 144)

    def test_03(self):
        self.assertEqual(solve(30), 832040)


if __name__ == '__main__':
    unittest.main(verbosity=2)



