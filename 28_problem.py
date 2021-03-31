'''Given a string s of words delimited by spaces, reverse the order of words.

Constraints

n ≤ 100,000 where n is the length of s
Example 1
Input
sentence = "hello there my friend"
Output
"friend my there hello" '''

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def reverse_sentence(n):
    pass


# DO NOT TOUCH THE BELOW CODE
class TestReverseSentence(unittest.TestCase):

    def test_01(self):
        self.assertEqual(reverse_sentence("hello there my friend"), "friend my there hello")

    def test_02(self):
        self.assertEqual(reverse_sentence("hello world"), "world hello")

    def test_03(self):
        self.assertEqual(reverse_sentence("welcome to class"), "class to welcome")


if __name__ == '__main__':
    unittest.main(verbosity=2)

