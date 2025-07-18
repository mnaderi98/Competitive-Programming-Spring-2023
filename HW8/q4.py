n, m = list(map(int, input().split()))
edges = [[] for i in range(n)]
first = 0
if m < n - 1:
    print("NO")
    exit()
for i in range(m):
    x, y = map(int, input().split())
    first = x - 1
    edges[x - 1].append(y - 1)
    edges[y - 1].append(x - 1)

def dfs(edges, i):
    first = i
    visited = [False for i in range(n)]
    stack = [first]
    while len(stack) != 0:
        temp = stack.pop()
        visited[temp] = True
        for i in edges[temp]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
    return visited
    

count = 0
for i in range(n):
    if len(edges[i]) % 2 == 1:
        count += 1

f = True
for i in range(n):
    if len(edges[i]) > 0:
        visited = dfs(edges, i)
        for x in range(n):
            if len(x) > 0 and not visited[x]:
                f = False
                break
        break
        
if (count == 0 or count == 2) and f:
    print("YES")
else:
    print("NO")
        
