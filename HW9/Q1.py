def dfs(node, graph, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, stack)
    stack.append(node)

def transpose(graph):
    transposed = [[] for _ in range(len(graph))]
    for node in range(len(graph)):
        for neighbor in graph[node]:
            transposed[neighbor].append(node)
    return transposed

def dfs_scc(node, graph, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_scc(neighbor, graph, visited)


def count_strongly_connected_components(graph):
    n = len(graph)
    visited = [False] * n
    stack = []
    for node in range(n):
        if not visited[node]:
            dfs(node, graph, visited, stack)
    transposed = transpose(graph)
    visited = [False] * n
    scc_count = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs_scc(node, transposed, visited)
            scc_count += 1

    return scc_count

v, e = map(int, input().split())

graph = [[] for _ in range(v)]

for _ in range(e):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)

scc_count = count_strongly_connected_components(graph)
print(scc_count)
