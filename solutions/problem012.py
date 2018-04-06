import math

from utils.numbers import get_prime_factors
from collections import Counter

num = 3
mdiv = 0
while True:
    # inp = math.pow(num,2)
    triangle = sum(range(int(num)))
    prime_factors = get_prime_factors(triangle)
    counts = Counter(prime_factors)
    div = reduce(lambda x, y: x*y, [i+1 for i in counts.values()])
    if div > 500:
        print num, triangle, div
        break
    num += 1
