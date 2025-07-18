def dijkstra(n, a, edges, source):
    needs = []
    power = 0
    visited = [False] * n
    stack = [(source, a[source])]
    visited[source] = True
    while stack:
        node, dist = min(stack, key=lambda x: x[1])
        stack.remove((node, dist))
        if node == source:
            power += dist
        elif power>dist:
            power += dist
        else:
            need = dist - power + 1
            needs.append(need)
            power += need + dist
        for (adj, dist2) in edges[node]:
            if not visited[adj]:
                stack.append((adj, dist2))
                visited[adj] = True
    return needs
                
n, m = map(int, input().split())
a = list(map(int, input().split()))
edges = [[] for i in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    edges[u-1].append((v-1, a[v-1]))
    edges[v-1].append((u-1, a[u-1]))
source = 0
distances = []
for source in range(n):
    needs = dijkstra(n, a, edges, source)
    distances.append(sum(needs))
print(*distances)
