from collections import deque
que = deque()
chain = {1:1}
counter = 0
counterI = 0

que.append(1)
while counter < 10 and que:
    i = min(que)
    que.remove(i)
    print i
    chain[2*i] = 1 + chain[i]
    if i < 12E9: que.append(2*i)
    if 2*i < 10:
        counter += 1
        if counter % 1000 == 0: print counter
    if (i-1) % 6 == 3 and (i-1)/3 not in chain:
        chain[(i-1)/3] = 1 + chain[i]
        if i < 12E9: que.append((i-1)/3)
        if (i-1)/3 < 10:
            counter += 1
            if counter % 1000 == 0: print counter
maximus = 0
print chain
for i in range(1,int(1E6)):
    print i
    if chain[i] > maximus:
        maximus = chain[i]

print maximus
