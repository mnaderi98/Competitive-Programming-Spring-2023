def dfs(n, visit, s):
    visit[s] = 1
    for i in range(len(n[s])):
        if visit[n[s][i]] == 0:
            if not dfs(n, visit, n[s][i]):
                return 0    
    return 1

v, e = map(int, input().split())
n = [[] for i in range(v+1)]
for i in range(e):
    a, b = map(int, input().split())
    n[a].append(b)
c = 0
for i in range(v):
    visit = [0 for i in range(v+1)]
    if dfs(n, visit, i) == 0:
        print("No")
        exit()

print("Yes")
