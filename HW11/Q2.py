import math

def op1(l, r, a, block_size, blocks):
    res = 0
    block_l = (l - 1) // block_size
    block_r = (r - 1) // block_size

    if block_l == block_r:
        for i in range(l - 1, r):
            res += a[i]
    else:
        for i in range(l - 1, (block_l + 1) * block_size):
            res += a[i]

        for i in range(block_l + 1, block_r):
            res += blocks[i]

        for i in range(block_r * block_size, r):
            res += a[i]

    print(res)

n, q = map(int, input().split())
a = list(map(int, input().split()))
block_size = int(math.sqrt(n))
blocks = [0] * ((n // block_size) + 1)

b = -1
c = 0
while c < n:
    if c % block_size == 0:
        b += 1
    blocks[b] += a[c]
    c += 1

for _ in range(q):
    op, l, r = map(int, input().split())
    if op == 1:
        op1(l, r, a, block_size, blocks)
    elif op == 2:
        blocks[(l - 1) // block_size] += (r - a[l - 1])
        a[l - 1] = r
