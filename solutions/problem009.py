# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math

trips = {}
for a in range(1,1000):
    for b in range(a,1000):
        c = math.sqrt(math.pow(a,2) + math.pow(b,2))
        if c == int(c):
            if a + b + c == 1000:
                print a*b*c
                break