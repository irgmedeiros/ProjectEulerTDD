# coding: utf-8

import unittest
from problem50 import *

"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""


class TestProblem50(unittest.TestCase):
    def test_prime_consecutive_bellow(self):
        self.assertEquals(MCPB(100), 41)
        self.assertEquals(MCPB(1000), 953)
        self.assertEquals(MCPB(10**6), 997651)


if __name__ == '__main__':
    unittest.main()
