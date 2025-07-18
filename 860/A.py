t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_a = max(a)
    max_b = max(b)
    count = 0

    if a[n-1] == max_a and b[n-1] == max_b:
        print('yes')
    elif a[n-1] == max_a:
        if max_b <= max_a:
            c = 0
            for i in range(n-1):
                if a[i] == b[i]:
                    c += 1
            if c == 0:
                print("yes")
            else:
                print("no")

        else:
            print("NO")
    elif b[n-1] == max_b:
        if max_a <= max_b:
            c = 0
            for i in range(n-1):
                if a[i] == b[i]:
                    c += 1
            if c == 0:
                print("yes")
            else:
                print("no")
    else:
        tmp = a[n-1]
        a[n-1] = b[n-1]
        b[n-1] = tmp
        if a[n-1] == max(a) and b[n-1] == max(b):
            print("yes")
        else:
            print("no")
