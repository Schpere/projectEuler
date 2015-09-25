from helpers import get_primes

num = 0
for i in get_primes():
    num += 1
    if num == 10001:
        print i
        break
