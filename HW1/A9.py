n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] > 3:
        print("*")
    else:
        print("*" * a[i])
