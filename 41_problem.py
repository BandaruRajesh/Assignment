"""
Write a Program to print only the numbers which starts with digit which is prime and end with digit which is divisible by 5 upto a given integer n

Example 1  
Input
n=5
Output
[5,20,25,30,35]

Example 2  
Input
n=10
Output
[5,20,25,30,35,50,55,70,75,200]
"""

import unittest


def PrimeDiv(nums):
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
class TestPrimeDiv(unittest.TestCase):

    def test_01(self):
        
        self.assertEqual(PrimeDiv(5),[5,20,25,30,35])

    def test_02(self):
        
        self.assertEqual(PrimeDiv(10),[5,20,25,30,35,50,55,70,75,200])

    


if __name__ == '__main__':
    unittest.main(verbosity=2)
