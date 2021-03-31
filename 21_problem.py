'''
Next Closest Odd Digit Number

Given an integer n, return the next closest integer where all digits are odd.
If there's two integers tied for being closest to n in absolute value, return the bigger integer.

Example 1:
Input:
n = 130

Output:
131

Explanation:
131 and 119 are the closest integers with all odd digits but 131 is bigger.

Example 2:
Input:
n = 2222

Output:
1999

Explanation:
1999 is closer than 3111
'''

#Implement the below function and run this file
# Return the output, No need to read input or print the output

def nxtClosestOdd(n):
    pass

#DO NOT TOUCH THE BELOW CODE

class TestnxtClosestOdd(unittest.TestCase):

    def test_1(self):
        self.assertEqual(nxtClosestOdd(130), 131)

    def test_2(self):
        self.assertEqual(nxtClosestOdd(2222), 1999)


if __name__ == '__main__':
    unittest.main(verbosity=2)