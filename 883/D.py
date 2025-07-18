t = int(input())

for j in range(t):
    n, b, h = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    minimum = 0
    values = []
    for i in range(n):
        if minimum > a[i]:
            values.append(minimum - a[i])
        minimum = a[i] + h
    result = b * h * n / 2
    number = sum(val**2 for val in values) * b / 2 / h
    result -= number
    print(result)
