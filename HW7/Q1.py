n = int(input())
adj = [[] for _ in range(n+1)]
sources = [0]*(n)
for i in range(n-1):
    a, b = map(int, input().split())
    adj[a].append((b, 0))
    adj[b].append((a, 1))
    sources[a - 1] += 1
if n == 1:
    print(0)
    print(1)
elif n == 2:
    print(0)
    if len(adj[0]) > 0:
        print(1, 2)
    else:
        print(2, 1)
else:
    # dfs
    dp = [0] * (n + 1)
    visited = [0] * (n + 1)
    stack = []
    i = 0
    cost = 0

    visited[1] = 1
    stack.append(1)

    while len(stack) ^ i:
        temp = stack[i]
        for node, price in adj[temp]:
            if not visited[node]:
                stack.append(node)
                visited[node] = 1
                if price > 0:
                    dp[node] = dp[temp] - 1
                    cost += 1
                else:
                    dp[node] = dp[temp] + 1
        i += 1

    min_price = min(dp)
    print(min_price+cost)
    print(*[dp[i] for i in range(1, n+1) if dp[i] == min_price])
    for i in range(1, n + 1):
        if dp[i] == min_price:
            print(i, end=" ")
