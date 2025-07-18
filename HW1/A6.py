n = int(input())
res = ['-'] * n
f3 = 1
fibs = [1]
f1 = 1
f2 = 1
while f3 <= n:
    res[f3 - 1] = '+'
    f3 = f1 + f2
    f1 = f2
    f2 = f3


for i in range(n):
    if i != len(res) - 1:
        print(res[i], end="")
    else:
        print(res[i])
