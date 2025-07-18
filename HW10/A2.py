n, q = map(int, input().split())
gordans = list(range(n))
rank = [0 for i in range(n+1)]
solders = [i for i in range(n+1)]
def find(x):
    if gordans[x] != x:
        gordans[x] = find(gordans[x])
    return gordans[x]

def merge(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    else:
        if rank[root_x] > rank[root_y]:
            gordans[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            gordans[root_x] = root_y
        else:
            gordans[root_y] = root_x
            rank[root_x] += 1

def op1(x, y):
    if find(x) != find(y):
        merge(x, y)

def op2(x, y):
    k = x
    while k < y:
        if solders[k] <= k:
            merge(k , k+1)
            solders[k] = max(y, solders[k])
            k+=1
        else:
            k = solders[k]
def op3(x, y):
    if find(x) == find(y):
        print("YES")
    else:
        print("NO")

for _ in range(q):
    op, x, y = map(int, input().split())
    if solders[x] != y and op == 1:
        op1(x, y)
    elif op == 2:
        op2(x, y)
    elif op == 3:
        op3(x, y)
exit()