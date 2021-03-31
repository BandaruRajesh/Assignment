'''
Longest Palindromic Subsequence

Given a string s with all lower case characters, find the length of the longest palindromic subsequence in s.

Example 1:
Input:
s = "rbaicneacrayr"

Output:
7

Explanation:
racecar is the longest palindromic subsequence of rbaicneacrayr

Example 2:
Input:
s = "chsoachrudeoe"

Output:
8

Explanation:
choeeohc is the longest palindromic subsequence of chsoachrudeoe

'''

#Implement the below function and run this file
# Return the output, No need to read input or print the output

def longBin(s):
    pass

#DO NOT TOUCH THE BELOW CODE

class TestlongBin(unittest.TestCase):

    def test_1(self):
        self.assertEqual(longBin("rbaicneacrayr"), 7)

    def test_2(self):
        self.assertEqual(longBin("chsoachrudeoe"), 8)


if __name__ == '__main__':
    unittest.main(verbosity=2)