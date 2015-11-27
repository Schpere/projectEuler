from math import factorial
n = factorial(9)
current = [0,9,8,7,6,5,4,3,2,1]
def neste(array):
    for i in range(1,len(array)):
        if array[-i] > array[-i-1]:
            return array[:-i-1] + [array[-i]] + sorted([array[-i-1]] + array[i+1:])


while n < 1E6:

    n += 1
    current = neste(current)
    print current

print current
