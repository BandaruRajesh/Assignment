"""
??? Program to update a dictionary ???
"""

import unittest


def dictup(d,d1):
    d.update(d1)
    return d


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestMethodName(unittest.TestCase):

    def test_dictupdate(self):
        d = {1:"apple",2:"banana"}
        d1 = {3:"orange"}
        newd={1:"apple",2:"banana",3:"orange"}

        self.assertEqual(dictup(d,d1),newd)


if __name__ == '__main__':
    unittest.main(verbosity=2)
