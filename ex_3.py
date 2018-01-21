def primeFactors(n):
    while n % 2 == 0:
        yield 2
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            yield i
            n = n / i
    if n >= 3:
        yield n

def primeFactorListMax(n):
    return max(primeFactors(n))

def ex_3():
    return primeFactorListMax(600851475143)

import math
import time
start_time = time.time()
print(ex_3())
print("--- %s seconds ---" % (time.time() - start_time))


# using the sieve of Eratosthenes