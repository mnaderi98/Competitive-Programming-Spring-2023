n, k = map(int, input().split())
v = 0
for i in range(n):
    v += int(input())
if v >= k:
    print("YES")
else:
    print("NO")
