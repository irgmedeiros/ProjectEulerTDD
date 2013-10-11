# coding: utf-8

"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import unittest
import problem1
import sys
import random


class TestProblem1(unittest.TestCase):
    def setUp(self):
        self.randomInt = (random.randint(0, sys.maxint))

    def test_multiple(self):
        self.assertEqual(problem1.multiple(3, 3), True)
        self.assertEquals(problem1.multiple(6, 3), True)
        self.assertEquals(problem1.multiple(3 * self.randomInt, 3), True)

    def test_multiples_of_zero(self):
        self.assertEquals(problem1.multiple(0, 3), True)

    def test_zero_as_multiple_of_one_number(self):
        self.assertRaises(ZeroDivisionError, problem1.multiple, *(3, 0))
        self.assertRaises(ZeroDivisionError, problem1.multiple, *(self.randomInt, 0))

    def test_multiples(self):
        self.assertEquals(list(problem1.multiples(9, 3)), [3, 6, 9])

    def test_multiples_of_3_or_5(self):
        self.assertEquals(list(problem1.multiples(9, 3, 5)), [3, 5, 6, 9])

    def test_sum_of_multiples_of_3_or_5(self):
        self.assertEquals(sum(problem1.multiples(10-1, 3, 5)), 23)

if __name__ == '__main__':
    unittest.main()
