'''
Next Closest Even Digit Number

Given an integer n, return the next closest integer where all digits are even.
If there's two integers tied for being closest to n in absolute value, return the bigger integer.

Example 1:
Input:
n = 151

Output:
200


Example 2:
Input:
n = 2222

Output:
2224

Explanation:
2220 and 2224 is closest but 2224 is choosen as 2224 is larger of two
'''

#Implement the below function and run this file
# Return the output, No need to read input or print the output

def nxtClosestEven(n):
    pass

#DO NOT TOUCH THE BELOW CODE

class TestnxtClosestOdd(unittest.TestCase):

    def test_1(self):
        self.assertEqual(nxtClosestEven(151), 200)

    def test_2(self):
        self.assertEqual(nxtClosestEven(2222), 2224)


if __name__ == '__main__':
    unittest.main(verbosity=2)