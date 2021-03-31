"""
WAP to to change the case of the letters of a "n" strings in such a way that if the length of the string is odd the capital
 letters in the word needs to be removed and small for even length.
Merge all the strings and print the difference  of alphabets present in strings before merging and after merging them.


Constraints

n < 100

Example 1
Input
ApPle
ORANGE
banaNa

Output
ple
ORANGE
N

Output should be displayed 7
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def solve(l):
    pass

class Ratiostrings(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(sovle(["ApPle","ORANGE","banaNa"]),7)

    def test_2(self):
        self.assertEqual(solve(["ORANGE"]),0)


if __name__ == '__main__':
    unittest.main(verbosity=2)