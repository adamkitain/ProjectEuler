from utils.numbers import gen_primes

d = gen_primes(2000000)
print sum(list(d))