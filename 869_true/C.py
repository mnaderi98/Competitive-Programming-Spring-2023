h, n = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[1 for _ in range(n)] for _ in range(n)]
if n > 2:
    dp[0][1] = 2
    dp[1][0] = 2

for i in range(n-2):
    j = i+2-1
    dp[i][j] = 2
    dp[j][i] = 2
for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        dp[i][j] = dp[i][j-1]
        fl = False
        for k in range(i, j + 1-3):
            if arr[k] <= arr[k+1] and arr[k+1] <= arr[k+2]:
                fl = True
        if fl == False:
            dp[i][j] += 1

for i in range(h):
    ks = list(map(int, input().split()))
    print(dp[ks[0]-1][ks[1]-1])
