# coding: utf-8


def fib_gen():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_sequence(number):
    seq = fib_gen()
    ans = []
    for n in xrange(number):
        ans.append(seq.next())
    return ans


def fibonacci(number):
    seq = fib_gen()
    for n in xrange(number - 1):
        seq.next()
    return seq.next() if number > 0 else 0


def problem2():
    seq = fib_gen()
    fib_number = 0
    ans = 0
    while fib_number < 4*10**6:
        fib_number = seq.next()
        if fib_number % 2 == 0:
            ans += fib_number
    return ans

    # return sum([x for x in seq if (x % 2 == 0 and x < 4*10**6)])
