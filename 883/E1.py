import math
t = int(input())
for i in range(t):
    n = int(input())
    v = int(math.sqrt(n))
    flag = True
    k = 2
    while k < v+1 and flag:
        x = 1
        while math.pow(k, x - 1) <= n:
            x += 1
        for i in range(1, x + 2):
            m = (math.pow(k, i) - 1) // (k - 1)
            if m == n:
                print("YES")
                flag = False
        k += 1
    if flag:
        print("NO")
