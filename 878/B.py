import math
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    min_index = n
    max_diff = 0
    diferences = []
    for i in range(n):
        if abs(p[i] - (i+1)) > 0:
            diferences.append(abs(p[i] - (i+1)))
    gcd = diferences[0]
    for i in range(1, len(diferences)):
        gcd = math.gcd(gcd, diferences[i])
    if gcd < n:
        print(gcd)
    else:
        print(0)
