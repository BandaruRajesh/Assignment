"""
Given a lowercase alphabet string s, return the total number of substrings that contain one unique character.

Constraints

n ≤ 10,000 where n is the length of s.
Example 1
Input
s = "aab"
Output
4
Explanation
These substrings have one unique character: ["a", "a", "aa", "b"]

"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def solve(s):
    pass

# DO NOT TOUCH THE BELOW CODE
class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(solve("dgoiowrbsnbrfnrpwnoptemenodlnbgfbvilbiuaeribuebeoatb"), 52)

    def test_02(self):
        self.assertEqual(solve("egwprhwobobadvidbgepqbpdnbpnhornibadpbphrposiveqiobpqbcsavfoveuvgoe"), 67)

    def test_03(self):
        self.assertEqual(solve("sionpwobpwoeppghaucxyatsdyvbjsvlfkhpsrojdlvsdvugoafsalcaksfa"), 61)


if __name__ == '__main__':
    unittest.main(verbosity=2)

