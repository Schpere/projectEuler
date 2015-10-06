def namescore(name):
    return sum(ord(i)-64 for i in name)

names = open('problem022.txt','r')

names = names.read().split(',')
names[-1] = names[-1][:-1]
names.sort()

print sum(namescore(names[i]) * (i+1) for i in xrange(len(names)))
