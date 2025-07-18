from collections import defaultdict

def is_eulerian(n, m, edges):
    # Create an adjacency list
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Check if all vertices have even degree
    for u in range(1, n+1):
        if len(adj_list[u]) % 2 == 1:
            return "NO"
    
    # Run a DFS to check if the graph is connected
    visited = [False] * (n+1)
    stack = [1]
    while stack:
        u = stack.pop()
        visited[u] = True
        for v in adj_list[u]:
            if not visited[v]:
                stack.append(v)
    
    if all(visited):
        return "YES"
    else:
        return "NO"

# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Check if the graph is Eulerian
print(is_eulerian(n, m, edges))
