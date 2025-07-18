from collections import deque

# تابع برای پیدا کردن بلندترین مسیر در گراف با استفاده از DFS
def dfs(start, graph):
    n = len(graph)
    visited = [False] * n
    max_dist = [-1] * n
    max_dist[start] = 0
    stack = deque([start])
    while stack:
        node = stack.pop()
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                max_dist[neighbor] = max_dist[node] + 1
                stack.append(neighbor)
    return max_dist.index(max(max_dist))

# خواندن ورودی
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

farthest_node = dfs(0, graph)

farthest_node = dfs(farthest_node, graph)

# چاپ طول قطر گراف
