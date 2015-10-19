from math import factorial
n = factorial(9)
current = [0,9,8,7,6,5,4,3,2,1]
def next(array):
    liste = array
    last = liste[-1]
    for i in range(len(liste)-1,-1,-1):
        if liste[i] < last:
            subarray = liste[i:]
            break
    print subarray
    temp = subarray[-1]
    for j in range(len(subarray)-1,-1,-1):
        subarray[j] = subarray[j-1]
    subarray[0] = temp
    liste[i:] = subarray
    print subarray
    return liste 

while n < 1E6:

    n += 1
