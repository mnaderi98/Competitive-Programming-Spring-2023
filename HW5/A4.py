k, n = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]


for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            next_p = dp[i][k] + dp[k + 1][j] + sum(arr[i: j + 1])
            dp[i][j] = min(dp[i][j], next_p)

print(dp[0][n-1])
