threes = range(0,1000,3)
fives = range(0,1000,5)
all = list(set(threes + fives))
print sum(all)