n = int(input())
a = list(map(int, input().split()))
first_choose = (0, 0)
out = 0
for i in range(n):
    for j in range(n-1, 0, -1):
        if a[i] == a[j] and j - i > first_choose[1] - first_choose[0]:
            first_choose = (i, j)
            out = 2
            break
    if first_choose != (0, 0):
        break
i = first_choose[0]+1

while i < first_choose[1]+1:
    j = first_choose[1]-1
    while j >= first_choose[0]:
        if i != j and a[i] == a[j]:
            first_choose = (i, j)
            out += 2
            break
        elif i == j and a[i] == a[j]:
            first_choose = (i, j)
            out += 1
            break
        j -= 1
    i += 1
print(out)
