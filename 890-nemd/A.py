t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = []
    for j in range(1, n):
        res.append(abs(a[j]-a[j-1]))
    res = sorted(res)
    result = 0
    m = n-k
    for k in range(m):
        result += res[k]
    print(result)