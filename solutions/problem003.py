# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math
from utils.numbers import gen_primes

magic_number = 600851475143

prime_numbers = gen_primes(math.sqrt(magic_number)+1)

factors = []
for p in prime_numbers:
    if magic_number % p == 0:
        factors.append(p)

print max(factors)
