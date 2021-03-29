"""
You are given a string s containing digits from "0" to "9" and lowercase alphabet characters. Return the sum of the numbers found in s.

Constraints

1 ≤ n ≤ 100,000 where n is the length of s
Example 1
Input
s = "11aa32bbb5"
Output
48
Explanation
Since 11 + 32 + 5 = 48.

"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def solve(s):
    pass


# DO NOT TOUCH THE BELOW CODE
class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(solve("1a2b30"), 33)

    def test_02(self):
        self.assertEqual(solve("abc"), 0)

    def test_03(self):
        self.assertEqual(solve("11ibiub13etpiwhigw878sdwrws87hs8h"), 997)


if __name__ == '__main__':
    unittest.main(verbosity=2)
