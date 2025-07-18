t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    bshtrn_ghdrat = 1
    while(bshtrn_ghdrat <= 1e9):
        bshtrn_ghdrat *= 2
    bshtrn_ghdrat -= 1

    kmtrin = bshtrn_ghdrat
    for j in range(n):
        kmtrin = kmtrin & a[i]
    
    res = 0
    new = bshtrn_ghdrat

    for k in range(n):
        new = new & a[i]
        if new == 0:
            res += 1
            new = bshtrn_ghdrat
    res += kmtrin > 0
    print(res)
  
    