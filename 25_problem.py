'''
Find Prefix

Given an input string s and a list of all possible words, return all words that have s as a prefix.

Example 1:

Input:
s = “re”
words = [“red”, “real”, “fear”]

Output:
[“red”, “real”]

Explanation:
Only real and red begin with re.

Example 2:

Input:
s = “b”
words = [“banana”, “biscuit”, “drip”, “blip”, “belt”]

Output:
[“banana”, “biscuit”, “blip”, “belt”]

Explanation:
All these words start with b, except for “drip”.
'''


# Implement the below function and run the program

def findPrefix(prefix, words):
    pass

# DO NOT TOUCH THE BELOW CODE

class TestfindPrefix(unittest.TestCase):

    def test_1(self):
        self.assertEqual(findPrefix('re', ['red', 'real', 'fear']), ['red', 'real'])

    def test_2(self):
        self.assertEqual(findPrefix('b', ['banana', 'biscuit', 'drip', 'blip', 'belt']), ['banana', 'biscuit', 'blip', 'belt'])


if __name__ == '__main__':
    unittest.main(verbosity=2)