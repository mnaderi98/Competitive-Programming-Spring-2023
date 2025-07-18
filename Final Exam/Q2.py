n = int(input())
graph = [[] for i in range(n)]
daraje = [0 for i in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
    daraje[u - 1] += 1
    daraje[v - 1] += 1
if n % 2 == 0:
    s = max(daraje)
    if s >= n//2:
        print(n - s - 1)
    else:
        print((n-1)//2)
else:
    print(-1)
        

    

