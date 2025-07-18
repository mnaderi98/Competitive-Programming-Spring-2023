import heapq

def dijkstra(graph, start, end, passport):
    n = len(graph)
    distances = [[float('inf')] * n for _ in range(2)]
    distances[0][start] = 0

    heap = [(0, start, False)]
    
    while heap:
        cost, node, has_passport = heapq.heappop(heap)
        curr_dist = distances[has_passport][node]
        
        if cost > curr_dist:
            continue
        
        for neighbor, weight, has_passport_neighbor in graph[node]:
            new_cost = cost + weight
            next_dist = distances[has_passport_neighbor][neighbor]
            
            if has_passport and not has_passport_neighbor:
                continue
            
            if new_cost < next_dist:
                distances[has_passport_neighbor][neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor, has_passport_neighbor))
    
    return min(distances[0][end], distances[1][end])

def find_minimum_cost(n, m, k, start_x, start_y, end_x, end_y, cells, embassies):
    graph = [[] for _ in range(n * m)]
    country_id = [[-1] * m for _ in range(n)]
    passport_node = set()
    
    # Create the graph
    for i in range(n):
        for j in range(m):
            node = i * m + j
            country = cells[i][j]
            is_passport_node = False
            
            if country in embassies:
                passport_node.add(node)
                is_passport_node = True
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = i + dx, j + dy
                
                if 0 <= nx < n and 0 <= ny < m:
                    neighbor = nx * m + ny
                    weight = 0
                    
                    if cells[nx][ny] != country:
                        weight = 1
                    
                    has_passport_neighbor = cells[nx][ny] in embassies
                    
                    if has_passport_neighbor and is_passport_node:
                        graph[node].append((neighbor, weight, has_passport_neighbor))
                    elif has_passport_neighbor:
                        graph[node].append((neighbor, weight + 1, has_passport_neighbor))
                    else:
                        graph[node].append((neighbor, weight, has_passport_neighbor))
            
            country_id[i][j] = country
    
    # Connect passport nodes with corresponding country nodes
    for node in passport_node:
        country = country_id[node // m][node % m]
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = node // m + dx, node % m + dy
            if 0 <= nx < n and 0 <= ny < m and country_id[nx][ny] == country:
                neighbor = nx * m + ny
                graph[node].append((neighbor, 0, True))
    
    # Run Dijkstra's algorithm
    start_node = (start_x - 1) * m + start_y - 1
    end_node = (end_x - 1) * m + end_y - 1
    return dijkstra(graph, start_node, end_node, False)

n, m, k = map(int, input().split())
start_x, start_y, end_x, end_y = map(int, input().split())

cells = []
for _ in range(n):
    row = list(map(int, input().split()))
    cells.append(row)

embassies = set()
for _ in range(k):
    x, y, p = map(int, input().split())
    embassies.add(p)

minimum_cost = find_minimum_cost(n, m, k, start_x, start_y, end_x, end_y, cells, embassies)
print(minimum_cost)
