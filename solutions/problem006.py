# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import math

print math.pow(sum(range(101)),2) - sum([math.pow(i,2) for i in range(101)])