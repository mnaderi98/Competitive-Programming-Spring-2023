import heapq

n = int(input())
s = input()
characters = [{} for _ in range(n + 10)]
dsts = {node: float('inf') for node in range(n + 10)}
for i in range(n):
    if i > 0:
        characters[i + 10][i + 9] = 1
    if i < n-1:
        characters[i+10][i+11] = 1
    characters[int(s[i])][i+10] = float(1/2)
    characters[i+10][int(s[i])] = float(1/2)

first = 10
last = n+9
dsts [first] = 0

pqueue = [(0, first)]

while len(pqueue) != 0:
    d, i = heapq.heappop(pqueue)

    if i == last:
        print(int(d))
        exit()

    if d > dsts [i]:
        continue

    for adj, w in characters[i].items():
        if (d + w) < dsts [adj]:
            dsts[adj] = d + w
            heapq.heappush(pqueue, (d + w, adj))

print(-1)
