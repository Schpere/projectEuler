from helpers import gcd

fractions = []
bigNum,bigDen = 1,1

for num in range(10,100):
    numerator = str(num)
    for a in range(1,10):
        if not '0' in numerator:
            if float(numerator)/int(str(a) + numerator[1]) == float(numerator[0])/a:
                fractions.append([num, int(str(a) + numerator[1])])
            if float(numerator)/int(numerator[1] + str(a)) == float(numerator[0])/a:
                fractions.append([num, int(numerator[1] + str(a))])
            if float(numerator)/int(str(a) + numerator[0]) == float(numerator[1])/a:
                fractions.append([num, int(str(a) + numerator[0])])
            if float(numerator)/int(numerator[0] + str(a)) == float(numerator[1])/a:
                fractions.append([num, int(numerator[0] + str(a))])

for fraction in fractions:
    if fraction[0] < fraction[1]:
        bigNum *= fraction[0]
        bigDen *= fraction[1]

print(bigDen/gcd(bigDen,bigNum))
