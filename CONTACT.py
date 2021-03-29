"""
You are given a two-dimensional list of strings contacts. Each element contacts[i] represents the list of emails for contact i. Contact i is considered a duplicate if there's a j < i such that contact j shares a common email with i. Return the number of unique people in contacts.

Constraints
0 ≤ n ≤ 100,000 where n is the total number of strings in contacts

Example 1
Input
contacts = [
    ["elon@tesla.com", "elon@paypal.com"],
    ["elon@tesla.com", "elon@spacex.com"],
    ["tim@apple.com"]
]
Output
2

Explanation
Contact 0 and 1 are the same person since they share a common email "elon@tesla.com". Then, contact 2 is another person.
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def solve(contacts):
    pass


# DO NOT TOUCH THE BELOW CODE
class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(solve([
    ["bill@microsoft.com"],
    ["jack@twitter.com"],
    ["jeff@amazon.com"]
]), 3)

    def test_02(self):
        self.assertEqual(solve([
    ["lawrence@gmail.com"],
    ["lawrence@gmail.com", "larry@gmail.com"],
    ["larry@gmail.com"]
]), 1)

    def test_03(self):
        self.assertEqual(solve([
    ["elon@tesla.com", "elon@paypal.com"],
    ["elon@tesla.com", "elon@spacex.com"],
    ["tim@apple.com"]
]), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)