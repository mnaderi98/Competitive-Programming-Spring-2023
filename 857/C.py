import sys
import random


def generate_blanket(n, m):
    rows = (n + 1) // 2
    cols = (m + 1) // 2

    submatrix_values = [
        [random.randint(0, (1 << 64)-1) for _ in range(4)] for _ in range(rows * cols)]

    blanket = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(rows):
        for j in range(cols):
            submatrix = submatrix_values[i*cols + j]
            for k in range(4):
                row = i*2 + (k//2)
                col = j*2 + (k % 2)
                blanket[row-1][col-1] = submatrix[k]

    if n % 2 == 1:
        for i in range(m):
            blanket[n-1][i] = blanket[n-2][i]
    if m % 2 == 1:
        for i in range(n):
            blanket[i][m-1] = blanket[i][m-2]

    return blanket


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    blanket = generate_blanket(n, m)
    count = []
    for i in blanket:
        count += i

    print(len(set(count)))
    for row in blanket:
        print(' '.join(map(str, row)))
