from helpers import sieve,primeQ
primes = sieve(1000000)
n = 1
divisors = 0
n_2 = 0

<<<<<<< HEAD
while divisors <= 500:
    if n % 2 == 0:
        n_1,n_2 = n_2,numFactors(n+1)
    else:
        n_1,n_2 = n_2,numFactors((n+1)/2)
    divisors = n_1*n_2
    n += 1
print n*(n-1)/2
