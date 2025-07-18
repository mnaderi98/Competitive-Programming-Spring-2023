import numpy as np
n = int(input())
p = list(map(int, input().split()))
# تعداد رای هر یک از مردم عادی: 0 تا ان منهای یک
# تعداد رای هر یک از مامورین مخفی:ان
# تعداد کل مردم عادی = X
# تعداد کل مامورین مخفی = Y
# min :        n*Y + (n-1) X = sum(p)
#             X + Y = 100
#             (n-1)* 100 + Y = sum(p)
#              Y = (sum(p) - 100*(n-1))
# max :
q = []
q.append(min(p))
s = 0
for i in p:
    s += i
y = s - ((n-1) * 100)
if y <= 0:
    q.append(0)
else:
    q.append(y)
h = sorted(q)
print(h[0], end=" ")
print(h[1])
