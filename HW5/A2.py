n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n+1)
res = 0
dp[0]
for i in range(2, n+1):
    dp[i] = min(a[i - 1] + dp[i - 1], a[i - 2] + dp[i - 2])
res = dp[n]
print(dp[n])
