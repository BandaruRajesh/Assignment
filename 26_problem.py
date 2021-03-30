'''

Find Suffix

Given an input string s and a list of all possible words, return all words that have s as a suffix.

Example 1:
Input:
s = “ge”
words = [“judge”, “hedge”, “stretch”]

Output:
[“judge”, “hedge”]

Explanation:
Only judge and hedge end with ed.

Example 2:
Input:
s = “mental”
words = [“sentimental”,  “monumental”, “mathematical”, “computational", “judgemental”]

Output:
[“sentimental”,  “monumental”, “judgemental”]

Explanation:
All these words end with mental, except for “mathematical” and “computational”.
'''

# Implement the below function and run the program

def findSuffix(suffix, words):
    pass

# DO NOT TOUCH THE BELOW CODE
class TestfindSuffix(unittest.TestCase):

    def test_1(self):
        self.assertEqual(findSuffix('te', ['mute', 'loot', 'mate']), ['mute', 'mate'])

    def test_2(self):
        self.assertEqual(findSuffix('e', ['state', 'plate', 'hate', 'jack', 'fate', 'nail']), ['state', 'plate', 'hate', 'fate'])


if __name__ == '__main__':
    unittest.main(verbosity=2)