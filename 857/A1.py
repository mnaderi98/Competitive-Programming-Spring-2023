t = int(input())
for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    manfi = len([num for num in b if num < 0])
    mosbat = len([num for num in b if num > 0])
    m1 = [x for x in range(1, mosbat+1)]
    for j in range(1, manfi+1):
        m1.append(mosbat-j)
    print(*m1)
    m2 = []

    for j in range(manfi):
        m2.append(1)
        m2.append(0)
    x = mosbat - manfi
    for j in range(1, x+1):
        m2.append(j)
    print(*m2)
