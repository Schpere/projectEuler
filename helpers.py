from itertools import takewhile,ifilter
from random import randrange,sample
from math import ceil 

#########################################################
#                                                       #
# Prime numbers and number theory                       #
#                                                       #
#########################################################

def gcd(a,b):
    while a > 0:
        r = b % a
        b = a
        a = r
    return b

def sieve(n):
    primeNumbers = range(n)
    primeNumbers[1] = 0
    for i in xrange(len(primeNumbers)):
        if primeNumbers[i] != 0:
            for k in xrange(2*i,n,i):
                primeNumbers[k] = 0
    return filter(lambda x : x != 0, primeNumbers)

def get_primes_w_sieve():
    prime_list = sieve(1000000)
    for i in prime_list:
        yield i
    n = prime_list[-1] + 2
    while True:
        for i in takewhile(lambda x : x <= n**.5, prime_list):
            if n % i == 0:
                break
        else:
            prime_list.append(n)
            yield n
        n += 2

def get_primes():
    prime_list = [2,3]
    for i in prime_list:
        yield i
    n = prime_list[-1] + 2
    while True:
        for i in takewhile(lambda x : x <= n**.5, prime_list):
            if n % i == 0:
                break
        else:
            prime_list.append(n)
            yield n
        n += 2

def primeFactor(n):
    if primeQ(n):
        return [n,1]
    factors = list()
    for p in get_primes_w_sieve():
        if n % p == 0:
            i = 1
            while n % pow(p,i+1) == 0:
                i += 1
            factors.append(p)
            factors.append(i)
            n /= pow(p,i)
            if n == 1:
                break
    return factors

def properFactors(n):
    if n == 1:
        return [1]
    else:
        factors = []
        for i in xrange(1,int(n**.5)+1):
            if n % i == 0:
                if i not in factors: factors.append(i)
                if i > 1 and n/i not in factors: factors.append(n/i)
    factors.sort()
    return factors

def numFactors(n):
    if n == 1:
        return 1
    factors = 1
    prime_exponents = primeFactor(n)
    for i in prime_exponents[1::2]:
        factors *= (i+1)
    return factors

def legendreSym(a,p):
    a = a % p
    if a == 0: return 0
    if p in get_primes():
        quads = [i**2 % p for i in range(1,int(p/2) + 1)]
        if a in quads: return 1
        return -1

def jacobiSym(a,n):
    fortegn = 1
    while a > 10 or n > 10:
        if a == 1 or n == 1:
            return fortegn
        elif a == 2:
            if (n % 8) in [1,7]:
                return fortegn
            return -fortegn
        elif a % n == 0:
            return 0
        elif a > n:
            a = a % n
        elif a % 2 == 0:
            if n % 8 not in [1,7]:
                fortegn *= -1
            a = a/2
        else:
            if (a % 4 == n % 4 == 3):
                fortegn *= -1
            a,n = n%a,a
    primes = [2,3,5,7]
    if n in primes:
        return fortegn * legendreSym(a,n)
    expon = [0,0,0,0]
    for i in range(len(primes)):
        while n % primes[i] == 0:
            n = n / primes[i]
            expon[i] += 1
    for i in range(len(primes)):
        fortegn *= (legendreSym(a,primes[i]))**expon[i]
    return fortegn

def primeQ(n):
    if n < 2**20:
        a_list = sample(range(2,n), min(n-2,10))
        for a in a_list:
            if jacobiSym(a,n) % n != pow(a,(n-1)/2,n):
                return False
        return True
    for _ in range(100):
        a = randrange(n)
        if jacobiSym(a,n) % n != pow(a,(n-1)/2,n):
            return False
    return True

def lcm_upto(n):
    product = 1
    for p in takewhile(lambda x : x <= n,get_primes()):
        i = 1
        while p**(i+1) <= n:
            i += 1
        product *= p**i
    return product

def factorFermat(n):
    N = n**.5
    if N % 1 == 0.0:
        return [int(N),2]
    N,i,t = ceil(N),1,0
    while t == 0:
        sigmaSquare = (N + i)**2 - n
        if sigmaSquare**.5 % 1 == 0.0:
            t = N + i
            s = sigmaSquare**.5
        i += 1
    return [int(t+s),1,int(t-s),1]


#########################################################
#                                                       #
# Sorting                                               #
#                                                       #
#########################################################


#########################################################
#                                                       #
# Special sequences and miscellania                     #
#                                                       #
#########################################################

def fibonacci(n):
    f_1,f_2 = 1,1
    while f_1 < n:
        yield f_1
        f_1,f_2 = f_2,f_1+f_2 
