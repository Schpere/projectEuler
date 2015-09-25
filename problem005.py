from helpers import prime_generator
from itertools import takewhile

primes20 = list()
for p in takewhile(lambda x : x < 20, get_primes()):
    primes20.append(p)

numbers = range(2,21)

factors = list()
for i in range(len(numbers)):
    factors[i] = 
