t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    opinions = [input() for _ in range(n)]
    num = 1
    for i in range(1, n):
        if opinions[0] == opinions[i]:
            num += 1

    print(num)
