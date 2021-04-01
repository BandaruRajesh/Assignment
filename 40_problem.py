"""
Write a Python Program to display the following series upto given inter n where n>0 and n<1000.

Example 1  
Input 
n=5
Output
[0,2,1,3,1]

Example 2  
Input 
n=10
Output
[0,2,1,3,1,5,2,7,3,11]

Hint: Check if the series is generating fibonacci and primes


"""

import unittest


def SeriesGen(nums):
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
class TestSeriesGen(unittest.TestCase):

    def test_01(self):
        
        self.assertEqual(SeriesGen(5), [0,2,1,3,1])

    def test_02(self):
        
        self.assertEqual(SeriesGen(10),[0,2,1,3,1,5,2,7,3,11] )



if __name__ == '__main__':
    unittest.main(verbosity=2)
