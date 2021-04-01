"""
Write a program to depict whether the given number is in the from of k*k where k is a prime number. 
Constraints :
1<input number≤105
INPUT CASE 1 :
Input : 25
Output : True
INPUT CASE 2 :
Input : 36
Output : False

"""

import unittest


def DepictNum(nums):
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
class TestDepictNum(unittest.TestCase):

    def test_01(self):
        

        self.assertEqual(DepictNum(25), True)

    def test_02(self):
        

        self.assertEqual(DepictNum(36), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
