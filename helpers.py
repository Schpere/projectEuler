from random import randrange
from random import sample

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
        else:
            if ([a % 4, n % 4] == [3,3]):
                fortegn *= -1
            a,n = n,a
    results = [[1,1,1,1,1,1,1,1,1,1],[1,0,-1,0,-1,0,1,0,1,0],[1,-1,0,1,-1,0,-1,-1,0,1],[1,0,1,0,1,0,1,0,1,0],[1,-1,-1,1,0,1,-1,-1,1,0],[1,0,0,0,1,0,-1,0,0,0],[1,1,1,1,-1,1,0,1,1,-1],[1,0,-1,0,-1,0,1,0,1,0],[1,1,0,1,1,0,1,1,0,1],[1,0,1,0,0,0,-1,0,1,0]]
    return fortegn*results[n+1][a+1]
#    primes = [2,3,5,7]
#    if n in primes:
#        quads = [i**2 % n for i in range(1,int(n/2)+1)]
#        if a % n in quads:
#            return fortegn
#        return -fortegn
#    for p in primes:
#       if n % p == 0:
#           return fortegn * jacobiSym(a,p) * jacobiSym(a,n/p)

def jacobiSymbol(a,n):
    if (a == 1 or n == 1):
        return 1
    elif (a % n == 0):
        return 0
    elif (a == 0):
        return 0
    elif (a == 2):
        if (n % 8) in [1,7]:
            return 1
        return -1
    elif (n > 2 and n % 2 == 0):
        if (a % 2 == 0):
            return 0
        return jacobiSymbol(a,2) * jacobiSymbol(a,n/2)
    elif (a > n):
        return jacobiSymbol(a % n,n)
    elif (a % 2 == 0):
        return jacobiSymbol(2,n) * jacobiSymbol(a/2,n)
    else:
        if (n % 4 == 3 and a % 4 == 3):
            return -jacobiSymbol(n,a)
        return jacobiSymbol(n,a)

def primeQ(n):
    if n < 2**40:
        a_list = sample(range(n), min(n,100))
        for a in a_list:
            if jacobiSym(a,n) % n != a**((n-1)/2) % n:
                return False
        return True
    for i in range(10):
        a = randrange(n)
        if jacobiSym(a,n) % n != a**((n-1)/2) % n:
            return False
    return True
