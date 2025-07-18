import math
n, k = map(int, input().split())

mod = 7 + (10 ** 9)

soorat = 1

makhraj = 1

try:
    for i in range(1, k+1):
        x = (soorat * (n - k + i))
        soorat = x % mod

    for i in range(1, k+1):
        x = (makhraj * i)
        makhraj = x % mod

    res = 1
    e = mod - 2

    while e > 0:
        if e % 2 == 1:
            res = (res * makhraj) % mod
        makhraj = (makhraj * makhraj) % mod
        e //= 2
    res = (soorat * res) % mod
    print(res)
except:
    print(math.factorial(n))
