n = int(input())
result = 0
borj = []
block_borj = []

for i in range(n):
    a = list(map(int, input().split()))
    borj.append(a.copy()[1:])


for i in range(n):
    block_borj.extend(borj[i])


block_borj.sort()
for i in range(len(borj)):
    new_b = []
    for k in borj[i]:
        idx = block_borj.index(k)
        new_b.append((k, idx))
    borj[i] = new_b.copy()


for i in range(len(borj)):
    b = borj[i]
    for k in range(len(b)-1):
        if b[k+1][1] - b[k][1] != 1:
            result += 1

print(result, n+result-1)
