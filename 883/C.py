MOD = 10**9 + 7

t = int(input())
for iii in range(t):
    new_values = []
    prev = 0
    new = 0
    n, m, h = map(int, input().split())
    for _ in range(n):
        values = list(map(int, input().split()))
        values = sorted(values)
        res = 0
        correct = 0
        s = 0
        for correct in range(m):
            s += values[correct]
            res += s
            if s > h:
                break
        if correct == m - 1:
            correct -= 1
        if s > h:
            correct -= 1
            res -= s
        new_values.append((correct, res))
        if len(new_values) == 1:
            new = res
            prev = correct
    new_values.sort(reverse=True, key=lambda x: (x[0], -x[1]))
    result = 0
    for i, element in enumerate(new_values):
        result += 1
        if element[1] == new and element[0] == prev:
            break
    print(result)
