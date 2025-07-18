t = int(input())
for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    indexes = []
    for f, elem in enumerate(b):
        indexes.append((elem, f))
    indexes = sorted(indexes)
    res = 0
    result = []
    if indexes[0][0] == indexes[n - 1][0]:
        print("0")
    elif 1 in b:
        print("-1")
    else:
        while(indexes[0][0] != indexes[n-1][0]):
            x = indexes[n - 1][1]
            y = indexes[0][1]
            result.append([x+1, y+1])
            h = int(indexes[n - 1][0]/indexes[0][0])
            if h == indexes[n - 1][0]/indexes[0][0]:
                indexes[n-1] = (h, indexes[n-1][1])
            else:
                indexes[n-1] = (h + 1, indexes[n-1][1])
            indexes = sorted(indexes)
            res += 1
        print(res)
        for k in range(res):
            print(result[k][0], " ", result[k][1])
