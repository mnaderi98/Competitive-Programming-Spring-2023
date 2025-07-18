import math


def divisor(n):
    i = 2
    for i in range(2, n):
        if n % i == 0:
            f[i] += 1
        j = i * i
        while j <= n:
            f[i] += 1
            j *= i


mod = (10 ** 9) + 7
a, b = map(int, input().split())
f = [0]*(b+1)
f[1] = 1
f[0] = 1
if a == b:
    print(1)
elif a == 0:
    h = 1
    for j in range(2, b+1):
        h *= j
    print(h)
else:
    n = 1

    h = 1
    for j in range(a, b+1):
        divisor(j)
    p = 0
    for j in range(2, len(f)):
        if j > 0:
            h = (h * (f[j]+1)) % mod

    print(h)
