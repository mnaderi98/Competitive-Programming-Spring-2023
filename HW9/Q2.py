n, q = list(map(int, input().split()))
parrents = list(map(int, input().split()))
dp = [(1, 0)]*(n+1)
j = 0

for i in range(2, n+1):
    dp[i] = (parrents[j], dp[parrents[j]][1]+1)
    j += 1

for i in range(q):
    node1, node2 = list(map(int, input().split()))
    p1, dp1 = dp[node1]

    p1, dp1 = node1, dp1+1

    p2, dp2 = dp[node2]

    p2, dp2 = node2, dp2+1

    while(p1 != p2):
        if(dp1 > dp2):
            p1, dp1 = dp[p1]
        else:
            p2, dp2 = dp[p2]

    print(p1)
