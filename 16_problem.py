'''
Smallest Gap

Given a list of integers n,
return the smallest difference of two consecutive integers in the sorted version of n.

Example 1:
Input:
n = [7, 1, 8, 11, 9, 12]
Output:
4
Explanation:
The smallest gap is between 8 and 9 is 1

Example 2:
Input:
n = [15, 12, 3, 22, 10, 17]
Output:
5
Explanation:
The largest gap is between 10 and 12 is 2
'''

#Implement the below function and run this file
# Return the output, No need to read input or print the output

def smallestGap(n):
    pass

#DO NOT TOUCH THE BELOW CODE

class TestlargestGap(unittest.TestCase):

    def test_1(self):
        self.assertEqual(smallestGap([14, 21, 22, 8, 29, 10]), 2)

    def test_2(self):
        self.assertEqual(smallestGap([15, 12, 13, 1, 100, 111]), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)