from helpers import get_primes

n = 600851475143

for i in get_primes():
    while n % i == 0:
        n = n / i
    if n == 1:
        print i
        break
