
def ex_1():
	return sum(set(range(3, 1000, 3)) | set(range(5, 996, 5)))

import time
start_time = time.time()
print(ex_1())
print("--- %s seconds ---" % (time.time() - start_time))

# Reason for using 3 as start -> we won't find a multiple of 3 below 3
# Reason for using 5 as start -> see above
# Reason for using 996 as end -> again same reason, but notice that range does not include 1000 or 996

# generator expressions are great: https://www.python.org/dev/peps/pep-0289/ (even better as list comprehensions)
# you can use list() + list() too, but I think it's more efficient staying with sets and do a union
# they conserve memory, which is important