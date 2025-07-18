n = int(input())
homes = input()
s, t = map(int, input().split())
if s > t:
    tmp = s
    s = t
    t = tmp
s = s-1
t = t-1
Hs = 0
i = s
while i <= t:
    x = i
    while i <= t and homes[i] == "H":
        i += 1
    y = i
    length = y - x
    one_nums = 0
    while length != 0:
        one_nums += length % 2
        length = (length // 2)
    Hs += one_nums
    i += 1
print(Hs)
