t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = len(bin(n))
    minix = a[0]
    indexes = []
    j = 0
    while j<n:
        minix = minix & a[j]
        if minix == 0 and j < n-2:
            indexes.append(j)
            minix = 1
        elif minix == 0:
            minix = 1
        j += 1

    print(len(indexes)+1)
    
    