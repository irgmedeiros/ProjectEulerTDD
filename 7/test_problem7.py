# coding: utf-8

import unittest
from problem7 import *

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


class TestProblem7(unittest.TestCase):
    def test_something(self):
        self.assertEqual(nth_prime(1), 2)
        self.assertEqual(nth_prime(2), 3)
        self.assertEqual(nth_prime(3), 5)
        self.assertEqual(nth_prime(4), 7)
        self.assertEqual(nth_prime(10001), 104743)


if __name__ == '__main__':
    unittest.main()
