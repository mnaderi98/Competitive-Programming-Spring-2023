n = int(input())
i = 0
x = n
m = 0
while x != 0:
    x = x >> 1
    m += 1

ones = []
num = 0
for i in range(m - 1, -1, -1):
    if n >= (2 ** (i)):
        num += (2 ** (i))
        n -= (2 ** (i))
        ones.append(i)
a = sorted(ones)
print(len(ones))
for i in range(len(a)):
    if i != len(a) - 1:
        print(a[i], end=" ")
    else:
        print(a[i])
