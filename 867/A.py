t = int(input())
for i in range(t):
    a = input()
    res = 1
    for i in range(len(a)):
        if i == 0 and a[0] == "0":
            res = 0
            break
        elif i == 0 and a[i] == "?":
            res *= 9
        elif a[i] == "?":
            res *= 10
    print(res)
