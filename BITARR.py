"""
You are given an integer list nums containing 0s and 1s. Consider an operation where we pick an index i in nums and flip i as well as all numbers to the right of i. Return the minimum number of operations required to make nums contain all 0s.

Constraints

n ≤ 100,000 where n is the length of nums.
Example 1
Input
nums = [1, 1, 0]
Output
2
Explanation
We can flip at index 0 to get [0, 0, 1] and then flip at index 2 to get [0, 0, 0]

"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def solve(nums):
    pass


# DO NOT TOUCH THE BELOW CODE
class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(solve([1,1]), 1)

    def test_02(self):
        self.assertEqual(solve([0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1]), 21)

    def test_03(self):
        self.assertEqual(solve([1,1,1,1,1,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1]), 29)


if __name__ == '__main__':
    unittest.main(verbosity=2)
