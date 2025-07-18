n = int(input())
a = list(map(int, input().split()))
mini = min(a)
mx = max(a)
jj = a.index(mx)
out = 0
if mini == mx:
    print(0)
else:
    mx_idx2 = 0
    while mx != mini:
        for i in range(jj, n):
            out += (mx - a[i])
        try:
            mx = max(a[mx_idx2:jj])
            mx_idx2 = a.index(mx)
            mini = min(a[mx_idx2:jj])
            tmp = jj
            jj = mx_idx2
            n = tmp
        except:
            mini = a[0]
            mx = a[0]
    print(out)
