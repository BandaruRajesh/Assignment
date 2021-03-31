"""
WAP to to change the case of the letters of a "n" strings in such a way that if the length of the string is odd the word is to be converted to upper case and lowercase for even length.
if the word ends with a vowel, then the last letter should be converted to upper case.
Merge all the strings and make sure the merged string is printed as well as the upper case and lower case letters seperately in a new line each.
store the entire result in a list
Constraints

n < 100

Example 1
Input
Apple Camera Tool

Output
APPLEcamerAtool
APPLEA
camertool
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def solve(n):
    '''
    implement the problem 
    '''
    
    pass

class VowelChangecase(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(solve("Apple Camera Tool"), ["APPLEcamerAtool","APPLEA","camertool"])

if __name__ == '__main__':
    unittest.main(verbosity=2)
