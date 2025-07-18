t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    arr = []
    i = 0
    while i < n:
        num = 0
        if s[i] == '<':
            while i<n and s[i] == '<':
                num += 1
                i += 1
            arr.append(num)
        elif i<n and s[i] == '>':
            while i<n and s[i] == '>':
                num += 1
                i += 1
            arr.append(num)
        

    res = max(arr) + 1
    print(res)


