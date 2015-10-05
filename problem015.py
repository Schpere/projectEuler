routes = [[int(i == 0 or j == 0) for i in range(21)] for j in range(21)]
print routes

for i in range(1,21):
    for j in range(1,21):
        routes[i][j] += routes[i-1][j] + routes[i][j-1]

print routes[-1][-1]
