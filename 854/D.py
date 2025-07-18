import numpy as np

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cold = list(map(int, input().split()))
    hot = list(map(int, input().split()))

    counts = [max(a.count(i + 1) - 1, 0) for i in range(k)]
    zarb = [counts[i] * hot[i] for i in range(len(hot))]
    s = np.sum(np.add(np.multiply(cold, np.int64(counts > 0)), zarb))

    print(s)
