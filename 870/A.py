t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    minimum = min(l)
    if n == 0:
        print(0)
    elif n == 1:
        if l[0] == 0:
            print(0)
        elif l[0] >= 1:
            print(-1)
    else:
        # res = l.count(minimum)
        layers = 0
        for x in range(n):
            counter = l.count(n - x)
            if counter > x:
                if x == 0 and counter == n:
                    pass
                else:
                    layers += counter
        if layers != 0:
            print(layers)
        elif minimum == 0 and layers == 0:
            print(0)
        elif layers == n:
            print(-1)
        else:
            print(-1)
