n= int(input())
edges = [[] for i in range(n)]
for i in range(n-1):
    x, y = map(int, input().split())
    first = x - 1
    edges[x - 1].append(y - 1)
    edges[y - 1].append(x - 1)
visited = [False for i in range(n)]
stack = [0]
temp = 0
distance = [-1 for i in range(n)]
distance[0] = 0
while len(stack) != 0:
    temp = stack.pop()
    visited[temp] = True
    for i in edges[temp]:
        if not visited[i]:
            stack.append(i)
            visited[i] = True
            distance[i] = distance[temp] + 1

visited = [False for i in range(n)]
last = distance.index(max(distance))
stack = [last]
dist = [-1 for i in range(n)]
dist[last] = 0
while len(stack) != 0:
    temp = stack.pop()
    visited[temp] = True
    for i in edges[temp]:
        if not visited[i]:
            stack.append(i)
            visited[i] = True
            dist[i] = dist[temp] + 1
print(max(dist))
            