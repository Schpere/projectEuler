from itertools import takewhile
from helpers import properFactors,primeQ

def isAbundant(i):
    if sum(properFactors(i)) > i: return True

numbers = [12]
i = 13
while i < 28123:
    for j in takewhile(lambda x : numbers[-1]*x < 28123,range(28123/12)):
        if numbers[-1]*j not in numbers:
            numbers.append(numbers[-1]*j)
    while (i in numbers) or (not isAbundant(i)):
        i += 1
    numbers.append(i)
numbers.sort()

integers = range(28123)
for i in numbers:
    for j in takewhile(lambda x: x + i < 28123 and x <= i, numbers):
        integers[i+j] = 0
print sum(integers)
