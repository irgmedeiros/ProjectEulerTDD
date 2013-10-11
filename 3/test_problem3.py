# coding: utf-8

import unittest
from problem3 import primes_less_than, largest_prime_factor

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


class TestProblem2(unittest.TestCase):
    def test_primes_less_than(self):
        """Obtain the set of primes numbers less than a given number"""
        self.assertEqual(primes_less_than(100),
                         set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]))

    def test_largest_factor(self):
        """Search the largest factor of a integer number"""
        self.assertEquals(largest_prime_factor(5), 5)
        self.assertEquals(largest_prime_factor(10), 5)
        self.assertEquals(largest_prime_factor(21), 7)
        self.assertEquals(largest_prime_factor(330), 11)
        self.assertEquals(largest_prime_factor(10001), 137)
        self.assertEquals(largest_prime_factor(600851475143), 6857)

if __name__ == '__main__':
    unittest.main()
