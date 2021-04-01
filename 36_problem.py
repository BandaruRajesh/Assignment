"""
Write a program to check whether the given input number n is in the given form or not, 
n=3x+2y.
Constraints:
1 ≤ n ≤104
INPUT CASE 1 :
Input : 12
Output : Yes   (3*2 + 2*3)
INPUT CASE 2 :
Input : 13
Output : Yes  (3*3 + 2*2)
INPUT CASE 3 :
Input : 1
Output : No 

"""

import unittest


def GivenForm(nums):
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
class TestGivenForm(unittest.TestCase):

    def test_01(self):
    
        self.assertEqual(GivenForm(12), "Yes")

    def test_02(self):
    
        self.assertEqual(GivenForm(13), "Yes")

    def test_03(self):
    
        self.assertEqual(GivenForm(1), "No")


if __name__ == '__main__':
    unittest.main(verbosity=2)
