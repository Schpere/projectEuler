from helpers import sieve,primeQ
primes = sieve(1000000)
n = 1
divisors = 0
n_2 = 0

while divisors < 1000:
    prime_divisors = list()
    n_1 = n_2
    while n >= 2*primes[-1]:
        p = primes[-1] + 2
        while not primeQ(p):
            p += 2
        primes.append(p)
    n_2 = n
    for p in primes:
        if n_2 % p == 0:
            prime_divisors.append(p)
            prime_divisors.append(2)
            n_2 /= p
        while n_2 % p == 0:
            n_2 /= p
            prime_divisors[-1] += 1
        if n_2 == 1:
            break
    n_2 = reduce(lambda x, y : x * y, prime_divisors[1::2],1)
    divisors = n_1*n_2
    n += 1
print n*(n-1)/2
