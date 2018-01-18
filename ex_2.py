def even_fib(n):
    f_zero, f_one = 0,1
    while f_zero < n:
        if f_zero % 2 == 0:
            yield f_zero
        f_zero, f_one = f_one, f_zero + f_one

def ex_2():
    return sum(even_fib(4000000))

import time
start_time = time.time()
print(ex_2())
print("--- %s seconds ---" % (time.time() - start_time))

# Here I wrote a generator function where the yield gives back results
# This is surprisingly fast in practice and yields ;) good results