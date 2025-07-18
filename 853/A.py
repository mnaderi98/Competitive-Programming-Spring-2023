import math
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    min_gcd = 1000
    for i in range(n):
        for j in range(i+1, n):
            gcd = math.gcd(a[i], a[j])
            if min_gcd > gcd:
                min_gcd = gcd
    if min_gcd <= 2:
        print("Yes")
    else:
        print("No")
