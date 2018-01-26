def findThePythagoreanTriplet(N):
    aMax = int(N/3)
    bMax = int(N/2)
    for a in range(aMax, 1, -1):
        for b in range(bMax, a, -1):
            c = N - (a+b)
            if c>b and a**2 + b**2 == c**2:
                return a, b, c

def ex_9():
    return reduce(mul,findThePythagoreanTriplet(1000))

import time
from operator import mul
from functools import reduce
start_time = time.time()
print(ex_9())
print("--- %s seconds ---" % (time.time() - start_time))

# a cannot be more as 333, so we don't have to start from 1000
# b cannot be more as 500, a minimal 1 and b 500 would be greater as c, which is not possible
# I included a check for c>b, which almost doubles the speed for the last if check