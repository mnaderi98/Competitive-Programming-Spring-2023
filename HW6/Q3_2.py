import math

MOD = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

for L in range(2, n+1, 2):
    for i in range(n-L+1):
        j = i + L - 1
        if L == 2:
            if a[i] > a[j]:
                dp[i][j] = 1
        else:
            for k in range(i+1, j+1, 2):
                if a[i] > a[k]:
                    if k == j:
                        dp[i][j] += dp[i+1][k-1]
                        dp[i][j] %= MOD
                    elif k == i + 1:
                        x = 1
                        y = int((j - k)/2)
                        step = (y + x) % MOD
                        dp[i][j] += dp[k+1][j] * dp[i][k] * step
                        dp[i][j] %= MOD
                    else:
                        x = int((k-i+1)/2)
                        y = int((j - k)/2)
                        num = min(x, y)
                        step = math.comb(x+y, num)
                        for l in range(1, num+1):
                            step = (step * (x+y+1-l) // l) % MOD
                        dp[i][j] += dp[i+1][k-1] * dp[k+1][j] * step
                        dp[i][j] %= MOD

print(dp[0][n-1])
