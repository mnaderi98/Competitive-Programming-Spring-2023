t = int(input())
for x in range(t):
    n = int(input())
    s = input()
    f = [1]*n
    l = [1]*n
    for i in range(1, n):
        h = 0
        for j in range(i):
            if s[i] == s[j]:
                h += 1
        if h > 0:
            f[i] = f[i - 1]
        else:
            f[i] = f[i - 1] + 1
    for i in range(n-2, -1, -1):
        h = 0
        for j in range(n-1, i, -1):
            if s[i] == s[j]:
                h += 1
        if h > 0:
            l[i] = l[i + 1]
        else:
            l[i] = l[i + 1] + 1

    max_value = 0
    for i in range(n):
        if i+1 < n and f[i] + l[i+1] > max_value:
            if i+1 < n:
                max_value = f[i] + l[i+1]
    print(max_value)
