'''
Circular Prime

Given an integer n, return whether every circular rotation of n is prime.

Example 1:
Input:
n = 113
Output:
True
Explanation:
113 is prime, 131 is prime, and 311 is prime.

Example 2:
Input:
n = 17
Output:
False
Explanation:
Even though 17 is prime, 71 is not.
'''

# Import this module
import math

#Implement the below function and run this file
# Return the output, No need to read input or print the output

def is_Prime(n):
    pass

def is_circular_prime(num):
    pass

#DO NOT TOUCH THE BELOW CODE

class Testis_circular_prime(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_rotating_prime(113), True)

    def test_2(self):
        self.assertEqual(is_rotating_prime(199), True)

    def test_3(self):
        self.assertEqual(is_rotating_prime(17), False)

    def test_4(self):
        self.assertEqual(is_rotating_prime(12), False)

    def test_5(self):
        self.assertEqual(is_rotating_prime(1193), True)

if __name__ == '__main__':
    unittest.main(verbosity=2)