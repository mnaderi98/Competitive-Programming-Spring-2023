t = int(input())


def isTrue(step, n):
    if n == 1:
        return True
    elif step > 40:
        return False
    elif n % 2 == 0:
        return False
    else:
        if isTrue(step + 1, (n - 1) // 2):
            path[step] = 2
            return True
        if isTrue(step + 1, (n + 1) // 2):
            path[step] = 1
            return True
    return False


for i in range(t):
    n = int(input())
    path = [0] * 40
    res = 0
    if isTrue(0, n):
        for j in range(40):
            if path[j] == 0:
                res = j
                break
        print(res)
        print(*reversed(path[:res]))
    else:
        print("-1")
