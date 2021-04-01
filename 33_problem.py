"""
??? program to remove spaces in a string ???
For example:
Input="j o h n"
Output="john"
"""

import unittest


def remove_space(string):
    return string.replace(" ", "") 

# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestMethodName(unittest.TestCase):

    def test_removespace(self):
        string="p r o g r a m"
        newstring ="program" 

        self.assertEqual(remove_space(string),newstring)


if __name__ == '__main__':
    unittest.main(verbosity=2)
