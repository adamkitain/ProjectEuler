import datetime as dt

counter = 0
for y in range(1901, 2001):
    for m in range(1,13):
        if dt.datetime(y,m,1).weekday() == 6:
            counter += 1
print counter