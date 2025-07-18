def has_common(a, b):
    x = 0
    y = 0
    z = 0
    l = 0
    for i in range(len(a) - 1):
        for j in range(len(b) - 1):
            if a[i] == b[j] and a[i+1] == b[j+1] and l <= 2:
                if l == 0:
                    x = i
                    y = j
                l += 2
                z += 1
                break
        if z == 1:
            break
    return (x, y, l)


t = int(input())
for i in range(t):
    a = input()
    b = input()
    import os
    if a[0] == b[0]:
        print("YES")
        print(f"{a[0]}*")
    elif a[len(a) - 1] == b[len(b) - 1]:
        print("YES")
        print(f"*{a[len(a)- 1]}")
    else:
        (x, y, size) = has_common(a, b)
        if size == 0:
            print("NO")
        else:
            print("YES")
            print(f"*{a[x: x+size]}*")
