n = int(input())
dp = [0] * n
dp[0] = 1
if n == 2:
    dp[1] = 2
elif n > 2:
    dp[1] = 2
    factorial = 2
    for i in range(2, n):
        factorial *= ((i+1) % 998244353)
        factorial %= 998244353
        dp[i] = (dp[i - 1] * (i+1) + (factorial - i - 1) % 998244353)
        dp[i] %= 998244353

print(dp[n-1])
