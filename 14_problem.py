'''
Add Binary Numbers

Given two strings a and b that represent binary numbers, add them and return their sum, also as a string.
The input strings are guaranteed to be non-empty and contain only 1s and 0s.

Example 1:
Input:
a = "1"
b = "1"

Output:
"10"

Example 2:
Input:
a = "111"
b = "1"

Output:
"1000"

'''

#Implement the below function and run this file
# Return the output, No need to read input or print the output

def addBinary(a,b):
    pass

#DO NOT TOUCH THE BELOW CODE

class TestaddBinary(unittest.TestCase):

    def test_1(self):
        self.assertEqual(addBinary("1", "1"), "10")

    def test_2(self):
        self.assertEqual(addBinary("111", "1"), "1000")

    def test_3(self):
        self.assertEqual(addBinary("110", "10"), "1000")

    def test_4(self):
        self.assertEqual(addBinary("1010", "1011"), "10101")


if __name__ == '__main__':
    unittest.main(verbosity=2)