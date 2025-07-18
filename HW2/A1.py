t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = a[0]
    count = 0
    for i in range(n):
        if a[i] >= (2*m - 1):
            if a[i] % ((m*2) - 1) == 0:
                count += int(a[i] / ((m*2) - 1)) - 1
            else:
                count += int(a[i] / ((m*2) - 1))

    print(count)
