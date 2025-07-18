n, m = map(int, input().split())
adj = [[] for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    adj[x - 1].append(y - 1)
    adj[y - 1].append(x - 1)
q = int(input())
for i in range(q):
    x, y = map(int, input().split())
    if x-1 in adj[y - 1]:
        print("NO")
    else:
        print("YES")
