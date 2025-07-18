t = int(input())
for _ in range(t):
    n = int(input())
    a= list(map(int, input().split()))
    bshtrin_ghdrt = 1
    res = 0
    while bshtrin_ghdrt <= 1e9:
        bshtrin_ghdrt *= 2
    bshtrin_ghdrt -= 1
    new = bshtrin_ghdrt
    kmtrin_gh = bshtrin_ghdrt
    for i in range(n):
        kmtrin_gh = kmtrin_gh & a[i]
    for i in range(n):
        new = new & a[i]
        if new == 0:
            new = bshtrin_ghdrt
            res += 1      
    res += kmtrin_gh > 0
    print(res)