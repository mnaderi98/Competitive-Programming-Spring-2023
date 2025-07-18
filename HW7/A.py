n = int(input())
edges = [[] for i in range(n+1)]
for i in range(n - 1):
    s, t = map(int, input().split())
    edges[s].append((t, 0))
    edges[t].append((s, 1))

stack = []
stack.append(1)
dp = [0] * (n + 1)
visited = [False] * (n + 1)
visited[1] = True
k = 0
cost = 0
while (len(stack) ^ k):
    temp = stack[k]
    for edge, price in edges[temp]:
        if (visited[edge] == False):
            stack.append(edge)
            visited[edge] = True
            if (price):
                dp[edge] = dp[temp]-1
                cost += 1
            else:
                dp[edge] = dp[temp]+1

    k += 1

min_price = min(dp)
print(min_price+cost)
for i in range(1, n + 1):
    if dp[i] == min_price:
        print(i, end=" ")
