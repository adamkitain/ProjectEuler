import math


def gen_primes(n):
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while q < n:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def triangle_nums(n):
    num = 1
    while num < n:
        yield sum(range(num+1))
        num += 1

def get_divisors(num):
    divisors = []
    for i in range(1,int(num/2)+1):
        if num % i == 0:
            divisors.append(i)
    divisors.append(num)
    return divisors

def get_prime_factors(num):
    factors = []
    primes = gen_primes(num+1)
    while num != 1:
        p = primes.next()
        while num % p == 0:
            num /= p
            factors.append(p)
    return factors