t = int(input())
for i in range(t):
    s = input()
    ch = "0"
    res = list(s)
    for i in range(len(s)):
        if s[i] == "?":
            res[i] = ch
        else:
            ch = s[i]

    print("".join(res))

        