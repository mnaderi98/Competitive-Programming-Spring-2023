t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = "NO"
    j = 0
    while j < n:
        if a[j] <= j + 1:
            result = "YES"
        j += 1
    print(result)
