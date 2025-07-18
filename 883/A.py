t = int(input())
#x>y cut
for i in range(t):
    n = int(input())
    res = 0
    for j in range(n):
        x, y = map(int, input().split())
        if x > y:
            res += 1
    print(res)