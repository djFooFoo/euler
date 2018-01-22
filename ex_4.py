def isPalindrome(numberString):
	if numberString == numberString[::-1]:
		return True
	return False

def ex_4():
	currentHighestProduct = 0
	product = 0
	for i in range(999, 100, -1):
		for j in range(999, 100, -1):
			product = i * j
			if product > currentHighestProduct and isPalindrome(str(product)):
				currentHighestProduct = product
	return currentHighestProduct

import time
start_time = time.time()
print(ex_4())
print("--- %s seconds ---" % (time.time() - start_time))

# This solution is fast enough, but you can go further than this

#The palindrome can be written as:
#abccba
#Which then simpifies to:
#100000a + 10000b + 1000c + 100c + 10b + a
#100001a + 10010b + 1100c
#11(9091a + 910b + 100c)

# This way you got to check 11 time less options (as the palindrome has to be divisable by 11)