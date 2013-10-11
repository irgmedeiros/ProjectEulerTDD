# coding: utf-8

import unittest
from problem35 import *

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""


class TestProblem35(unittest.TestCase):
    def test_circular_primes(self):
        self.assertEquals(list(circular_primes(100)), [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97])
        self.assertEquals(len(list(circular_primes(100))), 13)
        self.assertEquals(len(list(circular_primes(10**6))), 55)


if __name__ == '__main__':
    unittest.main()
