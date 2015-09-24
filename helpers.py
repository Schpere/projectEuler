def jacobiSymbol(a,n):
    if (a == 1):
        return 1
    elif (n <= 0 or (n % 2 == 0)):
        return 0
    elif (a == 2):
        if (n % 8) in [1,7]:
            return 1
        else:
            return -1
    if (a > n):
        if (a % 2 == 0):
            return jacobiSymbol(a % n,n)
        else:
            if (n % 4 == 3 and a % 4 == 3):
                return -jacobiSymbol(n,a)
            else:
                return jacobiSymbol(n,a)
    if (a % 2 == 0):
        return jacobiSymbol(2,n) * jacobiSymbol(a/2,n)
