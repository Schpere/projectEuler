def fibonacci(N = 0):
    i = 0
    n,m = 0,1
    while N == 0 or i < n:
        yield n
        n,m = m,n+m
        i += 1

n = 0
for i in fibonacci():
    if len(str(i)) == 1000:
        print n
        break
    n += 1
