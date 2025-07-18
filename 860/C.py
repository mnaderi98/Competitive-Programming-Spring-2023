def rearrange_array(n, a):
    a.sort()

    if a[0] >= 0 or a[-1] <= 0:
        return ["No"]

    pos_idx = [i for i in range(n) if a[i] > 0]
    neg_idx = [i for i in range(n) if a[i] < 0]

    result = [0] * n

    for i in range(len(pos_idx)):
        result[i * 2] = a[pos_idx[i]]
    for i in range(len(neg_idx)):
        result[i * 2 + 1] = a[neg_idx[i]]

    if len(pos_idx) > len(neg_idx):
        result[-1] = a[pos_idx[-1]]

    for i in range(n - 1):
        if abs(result[i] + result[i+1]) >= abs(a[0]):
            return ["No"]

    return ["Yes", " ".join(str(x) for x in result)]


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(*rearrange_array(n, a))
