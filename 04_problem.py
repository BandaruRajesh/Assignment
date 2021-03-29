'''Given a list of integers nums sorted in ascending order and an integer k, return whether any two elements from the list add up to k. You may not use the same element twice.
Constraints
n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [1, 3, 5, 8]
k = 6
Output
True
Explanation
We can have 1 + 5 = 6.
'''

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def solve(nums,k):
    pass

# DO NOT TOUCH THE BELOW CODE
class TestReverseSentence(unittest.TestCase):

    def test_01(self):
        self.assertEqual(solve([1, 3, 5, 8],7), False)

    def test_02(self):
        self.assertEqual(solve([1,6,24,55,89,234,1245],1246), True)

    def test_03(self):
        self.assertEqual(solve([12,34,56,66,6666,34982,1213414],66), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
