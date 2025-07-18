t = int(input())
for i in range(t):
    n = int(input())
    a = []
    b = []
    for j in range(n):
        f, h = map(int, input().split())
        a.append(f)
        b.append(h)
    a.sort()
    b.sort()
    m1 = a[n - 1]
    m2 = b[n - 1]
    pp = []
    xxx = 0
    if m1 > m2:
        pp.append(m1 - m2)
    else:
        pp.append(m2 - m1)

    if m1 < m2:
        if a[n - k] > m2:
            pp.append(a[n-k] - m2)
        elif b[n - k] > m1:
            pp.append(b[n-k] - m2)
    elif m2 < m1:
        if a[n - k] > m2:
            pp.append(a[n-k] - m2)
        elif b[n - k] > m1:
            pp.append(b[n-k] - m2)

    print(min(pp))
