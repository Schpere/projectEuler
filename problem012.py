from helpers import numFactors
n = 1
divisors = 0
n_2 = 0

while divisors <= 1000:
    n_1,n_2 = n_2,numFactors(n+1)
    divisors = n_1*n_2
    n += 1
print n*(n-1)/2
