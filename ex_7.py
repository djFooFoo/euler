def eratosthenes(n):
	upper_bound = int(n*(np.log(n)+np.log(np.log(n))))
	current = 1
	i = 1
	multiples = set()
	while current <= n:
		i += 1
		if i not in multiples:
			yield i
			current += 1
			for j in range(i*i, upper_bound, i):
				multiples.add(j)

def ex_7():
	return list(eratosthenes(10001))[-1]

import numpy as np
import time
start_time = time.time()
print(ex_7())
print("--- %s seconds ---" % (time.time() - start_time))

# p_n < n ln (n ln n) for n ≥ 6
# i*2 is not needed since we take out the even numbers at i = 2