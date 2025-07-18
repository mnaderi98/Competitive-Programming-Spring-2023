n, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    op, l, r = map(int, input().split())
    if op == 1:
        result = 0
        prev = 0
        l = l-1
        for i in range(l, r):
            result = min(result, prev+a[i])
            prev = min(prev+a[i], 0)
        print(result)
    elif op == 2:
        a[l - 1] = r
