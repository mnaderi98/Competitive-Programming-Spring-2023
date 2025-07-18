n, m, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [[0]*(n+1) for _ in range(n+1)]
for i in range(k):
    x, y, c = map(int, input().split())
    b[x][y] = c

dp = [[0]*(n+1) for _ in range(1 << (n+1))]

for i in range(1, n+1):
    dp[1 << (i-1)][i] = a[i]

max_satisfaction = 0
for c in range(1, 1 << (n+1)):
    num1 = 0
    for i in range(1, n+1):
        if c & (1 << (i-1)):
            num1 += 1
            for j in range(1, n+1):
                if not c & (1 << (j-1)):
                    dp[c | (1 << (j-1))][j] = max(dp[c | (1 << (j-1))][j], dp[c][i] + a[j] + b[i][j])
    if num1 == m:
        for i in range(1, n+1):
            if c & (1 << (i-1)):
                max_satisfaction = max(max_satisfaction, dp[c][i])

print(max_satisfaction)
