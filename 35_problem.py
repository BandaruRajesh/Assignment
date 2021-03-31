"""
Write a program which can return whether the String formed by combining the characters present in the input string is a palindrome or not.
Constraints :
1 ≤ length(i/p string) ≤ 100,000 
Ignore the case of characters present in the input string
INPUT CASE 1 :
Input : 1110a56b0233b1236A
Output : True
INPUT CASE 2 :
Input : 25694S23366a35652a222636s
Output : True
INPUT CASE 3 :
INPUT : 489k674a54654R
Output : False

"""

import unittest


def combinecharacters(s):
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
class TestCombinecharacters(unittest.TestCase):

    def test_01(self):
        
        self.assertEqual(combinecharacters("1110a56b0233b1236A"), True)
    def test_02(self):
        
        self.assertEqual(combinecharacters("25694S23366a35652a222636s"), True)
    def test_03(self):
        
        self.assertEqual(combinecharacters("489k674a54654R"), False)



if __name__ == '__main__':
    unittest.main(verbosity=2)
