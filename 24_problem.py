'''
Largest Gap

Given a list of integers n,
return the largest difference of two consecutive integers in the sorted version of n.

Example 1:
Input:
n = [4, 1, 2, 8, 9, 10]
Output:
4
Explanation:
The largest gap is between 4 and 8 is 4

Example 2:
Input:
n = [5, 2, 3, 1, 10, 11]
Output:
5
Explanation:
The largest gap is between 5 and 10 is 5
'''

#Implement the below function and run this file
# Return the output, No need to read input or print the output

def largestGap(n):
    pass

#DO NOT TOUCH THE BELOW CODE

class TestlargestGap(unittest.TestCase):

    def test_1(self):
        self.assertEqual(largestGap([4, 1, 2, 8, 9, 10]), 4)

    def test_2(self):
        self.assertEqual(largestGap([5, 2, 3, 1, 10, 11]), 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)