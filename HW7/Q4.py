n, k = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b = [int(i) for i in input().split()]
    adj[a].append(b)
    adj[b].append(a)


rows, cols = (n+1, k+1)
dp = [[0 for i in range(cols)] for j in range(rows)]
dp[1][0] = 1

stack = [(1, 0, 0)]
result = 0
# dfs
while len(stack) != 0:
    source, target, distance = stack.pop()
    if target < len(adj[source]):
        stack.append((source, target+1, distance))
        if adj[source][target] != distance:
            dp[adj[source][target]][0] = 1
            stack.append((adj[source][target], 0, source))
    else:
        if source == 1:
            break
        for i in range(k, 0, -1):
            dp[source][i] = dp[source][i-1]
        dp[source][0] = 0

        for i in range(k):
            result += dp[distance][i]*dp[distance][k-i]
            dp[distance][i] += dp[source][i]

print(result)
