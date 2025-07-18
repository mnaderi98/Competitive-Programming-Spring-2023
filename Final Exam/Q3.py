n = int(input())
prev = 3
if n == 2:
    print(prev)
    exit()
else:
    dp = [0 for i in range(n//2)]
    dp[0] = 1
    dp[1] = 3
    for i in range(2, n//2):
        dp[i] = ((3*dp[i-1]) + (3*dp[i-2]) - 1)%1000000007
        
print(dp[(n//2)-1])

