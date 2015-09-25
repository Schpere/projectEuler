from itertools import takewhile,ifilter
from random import randrange
from random import sample

#########################################################
#                                                       #
# Prime numbers and number theory                       #
#                                                       #
#########################################################

def sieve(n):
    primeNumbers = range(n)
    primeNumbers[1] = 0
    for i in xrange(len(primeNumbers)):
        if primeNumbers[i] != 0:
            for k in xrange(2*i,n,i):
                primeNumbers[k] = 0
    return filter(lambda x : x != 0, primeNumbers)

def get_primes():
    prime_list = sieve(100)
    for i in prime_list:
        yield i
    n = prime_list[-1] + 2
    while True:
        for i in prime_list:
            if n % i == 0:
                break
        else:
            prime_list.append(n)
            yield n
        n += 2

def legendreSym(a,p):
    a = a % p
    if a == 0: return 0
    if p in primes:
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
        a_list = sample(range(2,n), min(n,10))
        for a in a_list:
            if jacobiSym(a,n) % n != pow(a,(n-1)/2,n):
                return False
        return True
    for _ in range(100):
        a = randrange(n)
        if jacobiSym(a,n) % n != pow(a,(n-1)/2,n):
            return False
    return True

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
