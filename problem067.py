tree = list()

pyramid = open('problem067.txt','r')
for line in pyramid:
    tree.append([int(i) for i in line.split(' ')])

pyramid.close()

for line in range(len(tree)-2,-1,-1):
    for j in range(len(tree[line])):
        tree[line][j] += max(tree[line+1][j],tree[line+1][j+1])
print tree[0][0]

