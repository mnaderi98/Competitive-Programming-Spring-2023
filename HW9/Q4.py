def bfs_one(graph, start, end):
    visited = set()
    queue = [start]
    while queue:
        city = queue.pop(0)
        visited.add(city)
        if city == end:
            return True
        for neighbor in graph[city]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False
def bfs(graph, start, end, edges):
    graph[start].remove(end)
    for a, b in edges:
        if bfs_one(graph, a, b):
            pass
        else:
            graph[start].append(end)
            return 1
    return 0

n, m = map(int, input().split())

graph = [[j for j in range(n) if i!= j]for i in range(n)]
adj = [(i, j) for i in range(n) for j in range(n) if i != j]
edges = []

for _ in range(m):
    ai, bi = map(int, input().split())
    edges.append((ai-1, bi-1))
result = 0
for (ai, bi) in adj:
    result += bfs(graph, ai, bi, edges)
res = 0
for i in graph:
    res+=len(i)
print(res)
