def eratosthenes(n):
	i = 1
	multiples = set()
	while i < n-1:
		i += 1
		if i not in multiples:
			yield i
			for j in range(i*i, n, i):
				multiples.add(j)

from sympy import sieve
import numpy as np
import time
start_time = time.time()
#print(sum(eratosthenes(2000000)))
print(sum(sieve.primerange(1,2000000)))
print("--- %s seconds ---" % (time.time() - start_time))

# I used sieve of eratosthenes, but apparantly python (ofcourse) has a package for this. So I actually have two solutions, and I've put the slowest one in comment
# after all, we don't have to re-invent the wheel do we?