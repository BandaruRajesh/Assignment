'''
Longest Substring with 2 Distinct Characters

Given a string s, find the length of the longest substring that contains at most 2 distinct characters.

Example 1:
Input:
s = "abccb"

Output:
4

Explanation:
"bccb" is the longest substring with at most 2 distinct characters.

Example 2:
Input:
s = "abddddbcdccb"

Output:
6

Explanation:
"bddddb" is the longest substring with at most 2 distinct characters.
'''

#Implement the below function and run this file
# Return the output, No need to read input or print the output

def longestSub(s):
    pass

#DO NOT TOUCH THE BELOW CODE

class TestlongestSub(unittest.TestCase):

    def test_1(self):
        self.assertEqual(longestSub("abccb"), 4)

    def test_2(self):
        self.assertEqual(longestSub("abddddbcdccb"), 6)


if __name__ == '__main__':
    unittest.main(verbosity=2)