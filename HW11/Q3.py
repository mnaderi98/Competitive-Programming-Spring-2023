from math import ceil, log2


def op2(start, end, idx, x, diff):

    if (x < start or x > end):
        return

    tree[idx] = tree[idx] + diff

    if (start != end):
        mid = start + (end-start) // 2
        op2(start, mid, 2 * idx + 1, x, diff)
        op2(mid + 1, end, 2 * idx + 2, x, diff)

def op1(start, end, idx, l, r):

    if (l <= start and r >= end):
        return tree[idx]

    if (end < l or start > r):
        return 0

    mid = start + (end-start) // 2

    return (op1(start, mid, 2 * idx + 1, l, r) + op1(mid + 1, end, 2 * idx + 2, l, r))


n, q = list(map(int, input().split()))
arr = list(map(int, input().split()))

x = (int)(ceil(log2(n)))
tree = [0] * (2 * (int)(2**x) - 1)



for i in range(n):
    op2(0, n-1, 0, i, arr[i])


for _ in range(q):
    op, l, r = list(map(int, input().split()))
    if(op == 1):
        sum = op1(0, n-1, 0, l-1, r-1)
        print(sum)
    else:
        i, x = l-1, r
        op2(0, n-1, 0, i, x-arr[i])
        arr[i] = x
