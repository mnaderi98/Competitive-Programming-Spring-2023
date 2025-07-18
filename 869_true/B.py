t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
        continue
    if n == 2:
        print(1, 2)

    elif n % 2 == 1:
        print(-1)
    elif n % 2 == 0:
        x = []
        for i in range(1, n+1, 2):
            x.append(i+1)
            x.append(i)
        print(*x)
