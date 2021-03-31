'''

Clap Number

Given an integer n, return a list with each number from 1 to n,
but if it’s a multiple of 7 or has a 7 or 0 in the number, it should be replaced by the string “clap”.

Example 1:

Input:
n = 20

Output:
[“1”, “2”, “3”, “4”, “5”, “6”, “clap”, “8”, “9”, “clap”, “11”, “12”, “13”, “clap”, “15”, “16”,“clap”,“18”,“19”,“clap”]

Explanation:
- 7 and 14 were replaced by “clap” since they are divisible by 7.
- 17 is replaced since it has a 7 in the number.
- 10 and 20 were replaced since they had a 0 in the number.
'''


# Implement the below function and run the program

def clap_number(n):
    pass

# DO NOT TOUCH THE BELOW CODE

class TestClapNumber(unittest.TestCase):

    def test_1(self):
        self.assertEqual(clap_number(21), ["1", "2", "3", "4", "5", "6",
                                           "clap", "8", "9", "clap", "11", "12", "13", "clap", "15", "16", "clap", "18", "19", "clap", "clap"])

    def test_2(self):
        self.assertEqual(clap_number(7), ["1", "2", "3", "4", "5", "6",
                                           "clap"])

    def test_3(self):
        self.assertEqual(clap_number(39), ["1", "2", "3", "4", "5", "6", "clap", "8", "9", "clap", "11", "12", "13", "clap", "15", "16", "clap", "18", "19", "clap", "clap",
                                           "22", "23", "24", "25", "26", "clap", "clap", "29", "clap", "31", "32", "33", "34", "clap", "36", "clap", "38", "39"])

if __name__ == '__main__':
    unittest.main(verbosity=2)