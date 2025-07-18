t = int(input())
for i in range(t):
    n = int(input())
    s_p = list(map(str, input().split()))
    s_p = sorted(s_p, key=len, reverse=True)

    if s_p[0][1:] == s_p[1][:-1]:
        result = s_p[0] + s_p[1][-1]
    else:
        result = s_p[1] + s_p[0][-1]

    if result == result[::-1]:
        print("YES")
    else:
        print("NO")
