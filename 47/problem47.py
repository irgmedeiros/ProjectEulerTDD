# coding: utf-8
import collections


def factors(number):
    factors_list = []
    d = 2
    while number > 1:
        while number % d == 0:
            factors_list.append(d)
            number /= d
        d += 1
        if d * d > number:
            if number > 1:
                factors_list.append(number)
            break
    return factors_list


def numbers_with_n_factors(n):
    i = 2
    while 1:
        fact = collections.Counter(factors(i))
        if len(fact) == n:
            yield i, fact
        i += 1


def first_consecutive_n_all_diff_factors(n):
    gen = numbers_with_n_factors(n)
    lst = []

    #do
    last, factors = gen.next()
    lst.append(set(factors.items()))
    while 1:
        num, factors = gen.next()
        if num - last > 1:
            lst = [set(factors.items())]
            last = num
        else:
            lst.append(set(factors.items()))
            last = num

            if len(lst) == n and len(reduce(set.union, lst)) == (n * n):
                return range(num - n + 1, num + 1)





