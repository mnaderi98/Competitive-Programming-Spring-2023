n, m = map(int, input().split())
adj = []
for i in range(n):
    adj.append([])
    for j in range(n):
        adj[i].append(0)

for i in range(m):
    x, y = map(int, input().split())
    adj[x - 1][y - 1] = 1
    adj[y - 1][x - 1] = 1

for i in range(n):
    for j in range(n):
        if j == n-1:
            print(adj[i][j])
        else:
            print(adj[i][j], end="")
