def gcd(a, b):
    while b != 0:
        (a,b) = (b, a%b)
    return a

def lcm(a,b):
  return a * b / gcd(a,b)

def ex_5():
  return int(functools.reduce(lambda x,y: lcm(x,y), range(1,21)))

import functools
import time
start_time = time.time()
print(ex_5())
print("--- %s seconds ---" % (time.time() - start_time))

# reduce the problem to it's lowest complexity
# the lcm of 1 and 2 = 2
# the lcm of (lcm of 1 and 2) and 3 = lcm of 2 and 3 = 6
# the lcm of (lcm of (lcm of 1 and 2) and 3) and 4 = lcm of 6 and 4 = 12
# and so on... it's basically the lcm applied on a list