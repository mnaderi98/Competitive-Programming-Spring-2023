import heapq

n, m, t, k = map(int, input().split())

roads = [{} for _ in range(n + 1)]

dsts = [float('inf') for _ in range(n + 1)]


for _ in range(m):
    v, u, w = map(int, input().split())
    roads[v][u] = w
    roads[u][v] = w
cities = n

for _ in range(t):
    a = int(input())
    if dsts[a] >= k:
        cities -= 1
    dsts[a] = 0

    pqueue = [(0, a)]
    
    while pqueue:
        d, city = heapq.heappop(pqueue)
        
        if dsts[city] < d:
            continue
        
        for neighbor, road_cost in roads[city].items():
            distance = d + road_cost
            if dsts[neighbor] > distance and distance < k:
                if dsts[neighbor] >= k:
                    cities -= 1
                dsts[neighbor] = distance
                heapq.heappush(pqueue, (distance, neighbor))
    print(cities)
