for a in xrange(333):
    for b in xrange(a,500):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print a*b*c
            break
