"""
??? Program to convert list to set
 ???
 Example1 :
 input =[1,2,3,4]
 output={1,2,3,4}
 Example2 :
 input =[1,2,3,4,4]
 output={1,2,3,4}

"""

import unittest


def listtoset(listl):
    
    return set(listl)
# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestMethodName(unittest.TestCase):

    def test_listtoset(self):
        listl = [1, 2, 3, 4,4]
    
        

        self.assertEqual(listtoset(listl),set(listl))


if __name__ == '__main__':
    unittest.main(verbosity=2)
