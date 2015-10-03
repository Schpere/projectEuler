#chainlengths = {}
maxest = 0
best = 0
#for i in xrange(20):
#    chainlengths[2**i] = i

for i in xrange(1000):
    j = i
    this_terms = 0
    while j != 1:
#        if j in chainlengths:
#            this_terms = chainlengths[j] + this_terms - 1
#            j = 1
        if j % 2 == 0:
            j /= 2
        else:
            j = 3 * j + 1
        this_terms += 1
    if this_terms > maxest:
        best = i
        maxest = this_terms
#    if i < 500000:
#        chainlengths[i] = this_terms
print best
