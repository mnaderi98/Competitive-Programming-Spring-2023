t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    bshtrn_ghdrat = 1
    a = [0] + a
    res = 0

    for j in range(1, n+1):
        res = max(res, a[j])
    for j in range(1, n+1):
        out = a[j]
        for k in range(j+1, min(n, j+256)+1):
            out ^= a[k]
            res = max(out, res)
    print(res)