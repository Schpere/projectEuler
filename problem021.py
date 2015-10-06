from helpers import properFactors

summa = 0

for i in xrange(2,10000):
    j = sum(properFactors(i))
    if j != i and sum(properFactors(j)) == i:
        summa += i
print summa
