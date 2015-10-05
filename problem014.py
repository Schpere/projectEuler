from collections import deque
que = deque()
counter = 0

class Collatz:
    def __init__(self,value,parent):
        self.value = value
        if parent != None:
            self.level = 1 + parent.level
        else:
            self.level = 1
        self.parent = parent

lengths = [0 for _ in xrange(int(1E6))]
root = Collatz(1,None)
que.append(root)
longest = root

while counter < 1E6 and que:
    node = que.popleft()
    if node.value < 1E6:
        lengths[node.value - 1] = node.level
        if node.level > longest.level:
            longest = node
    if (node.value - 1) % 6 == 3 and node.value > 4:
        node.rightchild = Collatz((node.value - 1)/3,node)
        if node.rightchild.value < 1E6: counter += 1
        que.append(node.rightchild)
    node.leftchild = Collatz(node.value * 2,node)
    if node.leftchild.value < 1E6: counter += 1
    if node.leftchild.value < 1E3: que.append(node.leftchild)



print [i for i, e in enumerate(lengths) if e != 0]


maximus = longest.level
longValue = longest.value

for i in xrange(int(1E6)):
    length = lengths[i]
    if length == 0:
        j = i+1
        while True:
            length += 1
            if j % 2 == 0:
                j /= 2
            else:
                j = 3*j + 1
            if j < 1E6 and lengths[j-1] > 0:
                length += lengths[j-1]
                break
        lengths[i] = length
        if lengths > maximus:
            longValue = i+1
print max(xrange(len(lengths)),key=lengths.__getitem__) + 1
