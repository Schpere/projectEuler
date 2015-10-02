chainlengths = {}
maxest = 0
best = 0

for i in range(1000000):
    j = i
    this_terms = 1
    while j != 1:
        if j in chainlengths:
            this_terms = chainlengths[j] + this_terms - 1
            j = 1
        elif j % 2 == 0:
            j /= 2
        else:
            j = 3*j + 1
        this_terms += 1
    if this_terms > maxest:
        best = i
        maxest = this_terms
        chainlengths[best] = maxest
print best
