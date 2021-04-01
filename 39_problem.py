"""
Write a function that takes an integer n and returns the nth Prime number.

Example 1  
Input  
n=10
Output
29

Example 2
Input  
n=5
Output
11
"""

import unittest


def PrimeNum(nums):
    """
    ??? Write what needs to be done ???
    """
    pass


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestPrimeNum(unittest.TestCase):

    def test_01(self):
        self.assertEqual(PrimeNum(10), 29)

    def test_02(self):
        self.assertEqual(PrimeNum(5), 11)


if __name__ == '__main__':
    unittest.main(verbosity=2)
