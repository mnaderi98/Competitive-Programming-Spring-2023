MOD = int(1e9) + 7

t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)

    counter = 1
    j = 0
    for i in range(n):
        # j = 0
        while j < n and a[j] > b[i]:
            j += 1
        counter = (counter * (j - i)) % MOD

    print(counter)