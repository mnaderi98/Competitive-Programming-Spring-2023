t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    abar = list(map(int, input().split()))
    l = 0
    r = n-1
    for j in range(n):
        if a[j] != abar[j]:
            l = j
            break
    for j in range(n):
        if a[n-j-1] != abar[n-j-1]:
            r = n-j-1
            break
    r2 = r
    for j in range(r+1, n):
        if abar[j] >= abar[j - 1]:
            r2 = j
        else:
            break
    l2 = l
    for j in range(l-1, -1, -1):
        if abar[j] <= abar[j + 1]:
            l2 = j
        else:
            break

    print(l2+1, r2+1)
