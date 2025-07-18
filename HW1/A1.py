n = int(input())
res = 0
prev = 0
new = 0
for i in range(n):
    if i == 0:
        prev = int(input())
    else:
        new = int(input())
        if new != prev:
            res += 1
            prev = new
print(res)
