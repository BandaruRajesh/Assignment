"""
???Program to perform addition,subtraction and multiplication of two numbers ???
"""

import unittest

def add(x,y):
        return x+y
def sub(x,y):
        return x-y
def multiply(x,y):
        return x*y



# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestMethodName(unittest.TestCase):

    def test_add(self):
        
        self.assertEqual(add(10,5),15)
        self.assertEqual(sub(10,5),5)
        self.assertEqual(multiply(10,5),50)

if __name__ == '__main__':
    unittest.main(verbosity=2)
