"""
??? Program to remove duplicates in a given string ???
Example1:
    Input: Rom is Rom
    Output: Rom is
Example 2:
    Input: This is a better idea which is better
    Output:This is a better idea which is
"""

from collections import Counter
import unittest


def rm_dup(string):
   string = string.split(" ")
   for i in range(0, len(string)):
      string[i] = "".join(string[i])
      dupli = Counter(string)
      s = " ".join(dupli.keys())
   return s
   

# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestMethodName(unittest.TestCase):

    def test_remove_duplicates(self):
        string = "raju is a kid good kid"
        s = "raju is a kid good"

        self.assertEqual(rm_dup(string),s)


if __name__ == '__main__':
    unittest.main(verbosity=2)
