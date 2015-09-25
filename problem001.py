total = 0

for i in range(int(1000/3)+1):
    total += 3*i

for i in range(int(1000/5)):
    total += 5*i

for i in range(int(1000/15)+1):
    total -= 15*i

print total
