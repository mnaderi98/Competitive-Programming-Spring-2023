n, k = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b = [int(i) for i in input().split()]
    adj[a].append(b)
    adj[b].append(a)


rows, cols = (n+1, k+1)


stack = [(1, 0, 0)]
result = 0

dp = [[0 for i in range(cols)] for j in range(rows)]
dp[1][0] = 1

while len(stack) != 0:
    s, distance, target = stack.pop()
    if target < len(adj[s]):
        stack.append((s, distance, target+1))
        if adj[s][target] != distance:
            dp[adj[s][target]][0] = 1
            stack.append((adj[s][target], s, 0))
    else:
        if s == 1:
            break
        for i in range(k, 0, -1):
            dp[s][i] = dp[s][i-1]
        dp[s][0] = 0

        for i in range(k):
            result += dp[distance][i]*dp[s][k-i]
            dp[distance][i] += dp[s][i]

print(result)
