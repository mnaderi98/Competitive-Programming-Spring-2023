t = int(input())

for i in range(t):
    n, c, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    arr = [float('inf')] * (n+1)
    arr[0] = 0
    for i in range(1, n+1):
        

