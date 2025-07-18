from collections import defaultdict


def find_days(s, t, graph):
    queue = [(t, 0)] 
    visited = set([t])
    
    while queue:
        person, day = queue.pop(0)
        if person == s and day > 0:
            return day
        for friend in graph[person]:
            if friend != t and friend not in visited:
                visited.add(friend)
                queue.append((friend, day + 1))
    return -1

T = int(input())
for _ in range(T):
    n, m, s, t = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    days = find_days(s, t, graph)
    print(days)
