t = int(input())
for i in range(t):
    d, m, c = map(str, input().split())
    s = set()
    h = 0
    for x in m:
        if x == "+":
            s.add("+")
        elif x == "A":
            s.add("A")
        elif x == "B":
            s.add("B")
    for x in d:
        if x == "+":
            s.add("+")
        elif x == "A":
            s.add("A")
        elif x == "B":
            s.add("B")

    for x in c:
        if x == "+" and (x not in s):
            pass
        elif x == "A" and (x not in s):
            pass
        elif x == "B" and (x not in s):
            pass
        else:
            h += 1
    if h == len(c):
        print("valid")
    else:
        print("invalid")
