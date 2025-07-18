t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = max(a)
    y = min(a)

    maxim = 0
    if y < 0:
        a.remove(y)
        y2 = min(a)
        h1 = y2 * y
        a.remove(x)
        x2 = max(a)
        h2 = x * x2
        if h1 > h2:
            maxim = h1
        else:
            maxim = h2

    else:
        a.remove(x)
        x2 = max(a)
        maxim = x * x2
    print(maxim)
