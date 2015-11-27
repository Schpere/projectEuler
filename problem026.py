one = int(1e20)
longest = 6

for d in range(11,1000):
    temp = str(one/d)
    if len(str(1.0/d)) < longest:
        continue
    for j in range(1,len(temp)):
        if temp[0] == temp[j]:
            for 
