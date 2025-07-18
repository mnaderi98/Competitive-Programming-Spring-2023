n = int(input())
a = list(map(int, input().split()))
count = 0
# for i in range(n):
#     for j in range(n):
#         if i != j:
#             d = a[i] - a[j]
#             s = a[i] + a[j]
#             if d > s:
#                 count += 1
for i in a:
    if i < 0:
        count += 1
print(count * (n - 1))
