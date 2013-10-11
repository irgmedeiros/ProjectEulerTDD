# coding: utf-8

import pyprimes


def MCPB(num):
    """return prime that have the max consecutive prime sums bellow the specified number num"""

    #find top boundary
    primes = list(pyprimes.numpy_primes(num))

    hbound = 1
    searching = True
    while searching:
        s = sum(primes[:hbound])
        if s < num:
            hbound *= 2
        else:
            lbound = hbound / 2

            while True:
                old_hbound = hbound
                hbound = lbound + ((hbound - lbound) / 2)
                s = sum(primes[:hbound])
                if s < num:
                    lbound = hbound
                    hbound = lbound + ((old_hbound - lbound) / 2)
                    # hbound = old_hbound
                    if hbound == lbound:
                        hbound = old_hbound
                        searching = False
                        break

    highest_sequence = 0
    highest_prime = 0

    for pos, start_prime in enumerate(primes):
        for hs in xrange(hbound, start_prime, -1):
            sequence = primes[pos:hs]
            this_sum = sum(sequence)
            if this_sum in primes and (this_sum < num):
                if len(sequence) > highest_sequence:
                    highest_sequence = len(sequence)
                    highest_prime = this_sum
                    break

        #test if can be another higher sequence or not. Stop condition
        if hbound - pos < highest_sequence or pos == hbound:
            break

    return highest_prime




