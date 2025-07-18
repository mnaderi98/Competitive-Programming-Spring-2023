def is_super_permutation(p, n):
    b = [0] * n
    for i in range(n):
        b[i] = sum(p[:i+1]) % n
    return set(b) == set(range(n))


def generate_promising_permutation(n):
    p = list(range(1, n+1))
    while True:
        found_swap = False
        for i in range(n-1):
            if p[i] < p[i+1]:
                p[i], p[i+1] = p[i+1], p[i]
                if is_super_permutation(p, n):
                    found_swap = True
                    break
                else:
                    p[i], p[i+1] = p[i+1], p[i]
        if not found_swap:
            break
    if is_super_permutation(p, n):
        return p
    else:
        return -1


t = int(input())
for i in range(t):
    n = int(input())
    p = generate_promising_permutation(n)
    if p == -1:
        print(-1)
    else:
        print(*p)
