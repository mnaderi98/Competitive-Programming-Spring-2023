t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    s = input().strip()
    dp = []
    x = 0
    while x + 2 < n:
        if s[x] == s[x+1] or s[x] == s[x+2] or s[x+1] == s[x+2]:
            dp.append(x)
        x += 1
    dp.append(n)
    for _ in range(q):
        l, r = map(int, input().split())
        result = 0
        while dp[result] < l-1:
            result += 1
        if dp[result] + 2 <= r - 1:
            print("YES")
        else:
            print("NO")
