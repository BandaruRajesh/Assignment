'''
Minimum Distance of Two Words in a Sentence

Given the strings text, word0, and word1,
return the smallest distance between any two occurrences of word0 and word1
in text, measured in number of words in between.
If either word0 or word1 doesn't appear in text, return -1.

Example 1:
Input:
text = "dog cat hello cat dog dog hello cat world"
word0 = "hello"
word1 = "world"

Output:
1

Explanation:
There's only one word "cat" in between the hello and world at the end.
'''

#Implement the below function and run this file
# Return the output, No need to read input or print the output

def minDistance(text,word0,word1):
    pass

#DO NOT TOUCH THE BELOW CODE

class TestminDistance(unittest.TestCase):

    def test_1(self):
        self.assertEqual(minDistance("dog cat hello cat dog dog hello cat world","hello","world"), 1)

    def test_2(self):
        self.assertEqual(minDistance("mad bat chat mad bat mad chad bat mad mad chat bat chad","hello","world"), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)