import math

# 1 2 3 4   5  6  7  8  9  10
# 1 2 2 3   2  4  2  4  3  4
# 1 4 6 12 10 24 14  32 27 40


def divisor(n):
    i = 2
    res = 1
    f = [1]*(n+1)
    h = int(((n+1)*n)/2)
    counted = int((n//i) * (n//i) + 1)
    h += counted / 2

    return counted


n = int(input())
f = divisor(n)

print(f)
