t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    # top_down = []
    res = [-1] * n
    visited = [False] * (n + m)
    p = list(map(int, input().split()))
    r = 1
    j = n - 1
    for k in p:
        if visited[k - 1] == False and j >= 0:
            visited[k - 1] = True
            res[j] = r
            j -= 1
        r += 1
    for k in range(n):
        if k == n-1:
            print(res[k])
        else:
            print(res[k], end=" ")
