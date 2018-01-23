def differenceBetweenTheTwo(n):	
	sumOfSquares = sum(x**2 for x in range(1,n))
	squareOfSum = (sum(x for x in range(1,n)))**2
	return sumOfSquares - squareOfSum

def ex_6():
	return abs(differenceBetweenTheTwo(101))

import time
start_time = time.time()
print(ex_6())
print("--- %s seconds ---" % (time.time() - start_time))