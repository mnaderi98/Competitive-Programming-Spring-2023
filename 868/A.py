q = int(input())
for _ in range(q):
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    max_entertainment = -1
    result = -1

    for i in range(n):
        if a[i] <= t:
            if b[i] > max_entertainment:
                max_entertainment = b[i]
                result = i + 1
        t -= 1

    print(result)
