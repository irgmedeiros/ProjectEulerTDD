# coding: utf-8

import unittest
from problem47 import first_consecutive_n_all_diff_factors

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""


class TestProblem47(unittest.TestCase):
    def test_something(self):
        self.assertEquals(first_consecutive_n_all_diff_factors(2), [14, 15])
        self.assertEquals(first_consecutive_n_all_diff_factors(3), [644, 645, 646])
        self.assertEquals(min(first_consecutive_n_all_diff_factors(4)), [134043, 134044, 134045])


if __name__ == '__main__':
    unittest.main()
