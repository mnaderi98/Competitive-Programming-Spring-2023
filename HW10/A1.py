import random
edge = 0
class edgeClass:
    def __init__(self, s, d, w):
        self.src = s
        self.dest = d
        self.weight = w
    def __cmp__(self,y):
        return cmp(self.weight,y.weight)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union_one(i, sum):
    x = find(edges[i].src)
    y = find(edges[i].dest)
    if x != y:
        parent[x] = y
        present.append(i)
        sum += edges[i].weight
    return sum

def union_two(i, sum):
    x = find(edges[i].src)
    y = find(edges[i].dest)
    s = 0
    if x != y:
        parent[x] = y
        sum += edges[i].weight
        s += 1
    return sum , s
v, e = map(int, input().split())
parent = [i for i in range(v+1)]
present = []
edge = 0
edges = []
for i in range(e):
    s, d, w = map(int, input().split())
    edges.append(edgeClass(s, d, w))
edges = sorted(edges, key=lambda p: p.weight)

sum = 0
for i in range(e):
    sum = union_one(i, sum)

second_best = 1000000
sum = 0
for j in range(len(present)):
    parent = [i for i in range(v+1)]
    edge = 0
    for i in range(e):
        if i == present[j]:
            continue
        sum, s = union_two(i, sum)
        edge += s
    if edge != v-1:
        sum = 0
        continue
    if second_best > sum:
        second_best = sum
    sum = 0

if second_best == 1000000:
    print(-1)
else:
    print(second_best, '\n')


