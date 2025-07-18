def bfs(graph, start, end):
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)

    while queue:
        city, distance = queue.popleft()

        if city == end:
            return distance

        for neighbor in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1

def minimum_edges(n, queries):
    graph = [[] for _ in range(n)]
    edges = set()

    for a, b in queries:
        graph[a-1].append(b-1)
        edges.add((a-1, b-1))

    result = 0

    for a, b in edges:
        graph[a-1].remove(b-1)
        
        if bfs(graph, a-1, b-1) == -1:
            result += 1

        graph[a-1].append(b-1)

    return result
n, m = map(int, input().split())

edges = []
for _ in range(m):
    ai, bi = map(int, input().split())
    edges.append((ai-1, bi-1))

print(minimum_edges(n, edges))