t = int(input())
for k in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    for i in range(n - 1):
        while b[i + 1] % b[i] == 0:
            if b[i] == 1 or b[i] == b[i + 1]:
                b[i] += 1
            else:
                b[i+1] += 1
            if (i > 0 and b[i] % b[i - 1] == 0):
                b[i] += 1
    for j in range(n):
        if j != n-1:
            print(b[j], end=" ")
        else:
            print(b[j])
