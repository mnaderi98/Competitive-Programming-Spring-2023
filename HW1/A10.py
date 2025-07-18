A, B = map(str, input().split())
a = 0
b = 0
l = 0
for i in range(len(A)):
    if l == 1:
        break
    for j in range(len(B)):
        if A[i] == B[j]:
            a = i
            b = j
            l = 1
            break
row = ["."] * len(A)
res = []
for i in range(len(B)):
    res.append(row.copy())
for i in range(len(A)):
    res[b][i] = A[i]
for i in range(len(B)):
    res[i][a] = B[i]

for i in range(len(B)):
    for j in range(len(A)):
        if j != len(A) - 1:
            print(res[i][j], end="")
        else:
            print(res[i][j])
