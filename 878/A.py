t = int(input())

for _ in range(t):
    n = int(input())
    if n%2 == 0:
        a = [i*2 for i in range(1, n+1)]
    else:
        a = [i for i in range(1, n+1)]
    print(*a)
