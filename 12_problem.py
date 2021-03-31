"""
Given a string s, return its run-length encoding that is represent repeated successive characters as a single count and character.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.

Example 1:
Input:
s = "aaaabbbccdaa"

Output:
"4a3b2c1d2a"


Example 2:
Input:
s = "abcde

Output:
"1a1b1c1d1e"

"""

#Implement the below function and run this file
# Return the output, No need to read input or print the output

def runLengthEncode(s):
    pass

#DO NOT TOUCH THE BELOW CODE

class TestrunLengthEncode(unittest.TestCase):

    def test_1(self):
        self.assertEqual(runLengthEncode("aaaabbbccdaa"), "4a3b2c1d2a")

    def test_2(self):
        self.assertEqual(runLengthEncode("abcde"), "1a1b1c1d1e")

    def test_3(self):
        self.assertEqual(runLengthEncode("aabba"), "2a2b1a")

    def test_4(self):
        self.assertEqual(runLengthEncode("aaaaaaaaaa"), "10a")

    def test_5(self):
        self.assertEqual(runLengthEncode("asjjfdc"), "1a1s2j1f1d1c")


if __name__ == '__main__':
    unittest.main(verbosity=2)